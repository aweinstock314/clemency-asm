#!/usr/bin/env python2
from maps import *
from ins_class import *
from bitarray import *
import re
import sys
import struct

def encode(opcode, args):
    tmp = (op_bits[opcode] + args)
    print opcode, args, tmp
    (val, size) = enc_op_to_fun[opcode](*tmp)
    print val, bin(val), size
    assert val >= 0
    return (val, size)

class ParseException:
    def __init__(self, line, lineno, msg):
        self.line = line
        self.lineno = lineno
        self.msg = msg
    def __repr__(self):
        return 'ParseException on line %d: %s\n%r\n' % (self.lineno, self.msg, self.line)

MP_MODES = ['n','r','rw','e']
LITERAL_REGEX = '\+?(0b[01]+|0x[0-9a-fA-F]+|\d+)'
MEMORY_REGEX = r'^\[(r[0-9]+|pc|st|ra|fl)\s*\+\s*'+LITERAL_REGEX+',\s*'+LITERAL_REGEX+'\]$' # TODO: hex/bin offsets?

def parse(source):
    lines = source.split('\n')
    ast = []
    labels = {}
    for i, line in enumerate(lines, 1):
        line = line.split(';',1)[0].split('#',1)[0].strip() # comments
        match = re.match('^(\w+):\s*(.*)$', line)
        if match:
            label = match.group(1)
            labels[label] = len(ast)
            line = match.group(2)
        if not line:
            continue
        name, rest = (line + ' ').split(' ', 1)
        uf = False
        if name.endswith('.'):
            name = name[:-1]
            uf = True
        ops = []
        if rest.strip():
            limit = 1 if '[' in rest else -1 # hack for memory/delimiter ambiguity
            for op in rest.split(',', limit):
                op = op.strip().lower()
                # number (hex/int/bin literals) | r[0-31] | PC | ST | RA
                memory_match = re.match(MEMORY_REGEX, op)
                if memory_match:
                    reg, offset, regcount = memory_match.groups()
                    offset, regcount = int(offset, 0), int(regcount, 0)
                    ops.append(Mem(reg, offset, regcount))
                elif op in ['pc', 'st', 'ra', 'fl']:
                    ops.append(Reg(op))
                elif op in MP_MODES:
                    lit = MP_MODES.index(op)
                    ops.append(Imm(lit))
                elif re.match('^r[0-9]+$', op):
                    ops.append(Reg(op))
                elif re.match(r'^'+LITERAL_REGEX+'$', op):
                    lit = int(op, 0)
                    ops.append(Imm(lit))
                elif re.match(r'^&\w+$', op):
                    ops.append(Label(op[1:]))
                else:
                    raise ParseException(line, i, "Invalid operand %r" % (op,))
        if name in ['db', 'dw', 'dt']:
            nytes = []
            for op in ops:
                nytes.extend(op.untyped_repr(None))
            ast.append(RawNytes(nytes))
        else:
            ast.append(Ins(name, uf, ops))
    return (ast, labels)

def assemble(ast, labels):
    def do_pass(data):
        values = []
        sizes = []
        for (i, instr) in enumerate(ast):
            (value, size) = instr.emit(data, i)
            values.append(value)
            sizes.append(size)
        return (values, sizes)

    # first pass calculates sizes
    (_, sizes) = do_pass(None)

    # second pass uses sizes for labels, accumulates generated instructions
    (values, _) = do_pass((labels, sizes))

    outputs = []
    for (value, size) in zip(values, sizes):
        nytes = []
        for i in range(size):
            nyte = value >> (9*i)
            nyte = nyte & ((1<<9)-1)
            nytes.append(nyte)
        nytes.reverse()
        swapendian(nytes)
        outputs.append(nytes)
    return outputs

def swapendian(nytes):
    'swap endian (2, 1, 3, 2, 1, 3)'
    if len(nytes) >= 2:
        nytes[0], nytes[1] = nytes[1], nytes[0]
    if len(nytes) >= 5:
        nytes[3], nytes[4] = nytes[4], nytes[3]

def nytes_to_bytes(ins_list):
    ba_full = bitarray()
    for ins in ins_list:
        for nyte in ins:    
            ba = bitarray()
            ba.frombytes(struct.pack('>H', nyte))
            ba = ba[7:]
            ba_full += ba
            
    return ba_full.tobytes()
            
def tests():
    asm = '''
AD. r1, r3, r2
foo:
MUF r0, r5, r10
BLE &foo
HT
dt 41, 42, 43
db 0xff
dw 0xfff, 0xfff
'''
    print(asm)
    ast, labels = parse(asm)
    print(labels)
    print(ast)
    print('\n'.join(map(str, ast)))
    mc = assemble(ast, labels)
    print(mc)

if __name__ == '__main__':
    if len(sys.argv) == 3:
        with open(sys.argv[1], 'r') as f:
            asm = f.read()
            ast, labels = parse(asm)
            #print ast, labels
            output = assemble(ast, labels)
            print(output)
        with open(sys.argv[2], 'w') as f2:
            f2.write(nytes_to_bytes(output))
    else:
        tests()
