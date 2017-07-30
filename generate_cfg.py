from pprint import *
from subprocess import *
#import graphviz as gv

def hlt(mnem): return instr_eq(mnem, "ht")
def ret(mnem): return instr_eq(mnem, "re")
def ubr(mnem): return instr_eq(mnem, "b")
def cbr(mnem): return not ubr(mnem) and not instr_eq(mnem, "bf") and not instr_eq(mnem, "bfm") and mnem.split()[0][0] == 'b'
def call(mnem): return mnem.split()[0][0] == 'c'and not instr_eq(mnem, "cm") and not instr_eq(mnem, "cmf") and not instr_eq(mnem, "cmfm") and \
                                                    not instr_eq(mnem, "cmim") and not instr_eq(mnem, "cmi") and not instr_eq(mnem, "cmm")
def terminate(mnem): return hlt(mnem) or ubr(mnem) or cbr(mnem) or ret(mnem)

def make_disassembler(fname):
    try:
        # git clone git@github.com:ppr-ctf/asm.git
        # export PYTHONPATH=$(readlink --canonicalize ./asm)
        import asm
        import asm.disassembler
        with open(fname, 'r') as f:
            bytes = f.read()
        from asm.bits import bits2nytes, bytes2bits
        from asm.ins_class import branch_ops
        nytes = bits2nytes(bytes2bits(bytes))
        def disass(addr):
            try:
                output = asm.disassembler.disassemble_nytes(nytes[addr:], limit=1)
                instr = output[0]
                link = instr.location(addr)
                #print '%08x: "%s", %r, %r' % (addr, output[0], terminate(output[0].name), ('%08x' % link if link else link))
                return instr.size(), str(instr), link, instr
            except Exception:
                sys.stderr.write('Disassembly failed at %#x, bailing on that bb (rest of worklist will still be processed)\n' % addr)

        def instr_eq(mnem, instr):
            return mnem.split()[0] == instr or \
                   mnem.split()[0] == instr + "."

        return disass, instr_eq
    except ImportError:
        def instr_eq(mnem, instr):
            return mnem.split()[0] == instr + "\x00" or \
                   mnem.split()[0] == instr + "."

        def readuntil(p, needle):
            ret = ""
            while needle not in ret:
                ret += p.stdout.read(1)
            return ret

        p = Popen(['./clemency-emu', '-d', '0', fname], stdin=PIPE, stdout=PIPE)
        readuntil(p, ">")

        def disass(addr):
            p.stdin.write('u {} 2\n'.format(hex(addr)[2:]))
            readuntil(p, "\n")
            addr1 = readuntil(p, "\n").rstrip()
            addr2 = readuntil(p, "\n").rstrip()
            size = int(addr2[:7], 16) - addr
            if "(" in addr1:
                link = int(addr1[addr1.find("(")+1:addr1.find(")")], 16)
            else:
                link = None
            mnem = addr1[len("0000000:                         2b0402000002b8  ")+3:]
            #print addr, mnem
            return size, mnem, link, None
        return disass, instr_eq


def construct_cfg(bbs, graph, addr, disass, call_targets, call_triples):
    worklist    = [ ]
    if addr in bbs:
        return
    bbs[addr]   = [ ]
    graph[addr] = [ ]
    bb = bbs[addr]
    gg = graph[addr]
    startaddr = addr
    while True:
        result = disass(addr)
        if result:
            size, mnem, link, instr = result
            bb.append("{}: {}".format(hex(addr), mnem))
            if instr is not None and instr.name == 'ml':
                out2 = disass(addr+size)
                if out2 and out2[3] and out2[3].name == 'mh':
                    lo = instr.ops[-1].value
                    hi = out2[3].ops[-1].value
                    val = lo & ((1 << 10) - 1)
                    val |= hi << 10
                    bb.append("# mh/ml pair yields %x" % val)
            if link is not None:
                worklist.append(link)
            if call(mnem) and link is not None:
                call_targets.append(link)
                call_triples.append((startaddr, link, addr))
            addr += size
            if terminate(mnem):
                break
        else:
            bb.append("# BB terminated by an invalid instruction")
            return
    if cbr(mnem):
        worklist.append(addr)
        gg.append(addr)
        bb.append("(fall through {})".format(hex(addr)))
    if ubr(mnem) or cbr(mnem):
        gg.append(link)
    for i in worklist:
        construct_cfg(bbs, grp, i, disass, call_targets, call_triples)

# GRAPHVIZ OUTPUT STUFF
styles = {
    'graph': { 'fontname': 'monospace', },
    'nodes': { 'fontname': 'monospace', },
    'edges': { 'fontname': 'monospace', }
}

def apply_styles(graph, styles):
    graph.graph_attr.update(('graph' in styles and styles['graph']) or {})
    graph.node_attr.update(('nodes' in styles and styles['nodes']) or {})
    graph.edge_attr.update(('edges' in styles and styles['edges']) or {})
    return graph

if __name__ == '__main__':

    import sys
    fname = 'hello.bin'
    if len(sys.argv) == 2:
        fname = sys.argv[1]
    disass, instr_eq = make_disassembler(fname)

    bbs = { }
    grp = { }
    call_targets = [ ]
    call_triples = []
    construct_cfg(bbs, grp, 0, disass, call_targets, call_triples)


    if '--graphviz' in sys.argv:
        g1 = apply_styles(gv.Digraph(format='svg', node_attr={"shape":"box"}), styles)
        for i in bbs:
            if i in call_targets:
                g1.node(hex(i),
                        label="\l".join(bbs[i]).replace("\x00", "") + "\l",
                        color='red')
            else:
                g1.node(hex(i),
                        label="\l".join(bbs[i]).replace("\x00", "") + "\l")
        for i in grp:
            for j in grp[i]:
                g1.edge(hex(i), hex(j))
        call_counts = {}
        for (sourcebb, destbb, sourceinst) in call_triples:
            g1.edge(hex(sourcebb), hex(destbb), color='red', label=hex(sourceinst))
            call_counts[destbb] = call_counts.get(destbb, 0) + 1
        (lambda s: g1.node(s, label=s+"\l"+"\l".join("%s: %d" % (hex(destbb), count) for (destbb, count) in sorted(call_counts.items(), key=lambda x: x[1], reverse=True))))("bb's by call quantity:")
        print g1.source
        # g1.render()
    else:
        for b in bbs:
            print "===",hex(b),"==="
            for cmd in bbs[b]:
                print cmd.replace("\x00","")
