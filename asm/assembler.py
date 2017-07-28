#!/usr/bin/env python2
from maps import *
from ins_class import *
from bitarray import *
import re
import sys
import struct

def encode(opcode, args):
    return enc_op_to_fun[opcode](*(op_bits[opcode] + args))

class ParseException:
    def __init__(self, line, lineno, msg):
        self.line = line
        self.lineno = lineno
        self.msg = msg
    def __repr__(self):
        return 'ParseException on line %d: %s\n%r\n' % (self.lineno, self.msg, self.line)

LITERAL_REGEX = '(0b[01]+|0x[0-9a-fA-F]+|\d+)'
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
                elif re.match('^r[0-9]+$', op):
                    ops.append(Reg(op))
                elif re.match(r'^'+LITERAL_REGEX+'$', op):
                    lit = int(op, 0)
                    ops.append(Imm(lit))
                elif re.match(r'^&\w+$', op):
                    ops.append(Label(op[1:]))
                else:
                    raise ParseException(line, i, "Invalid operand %r" % (op,))
        ast.append(Ins(name, uf, ops))
    return (ast, labels)

def assemble(ast, labels):
    # first pass calculates sizes
    sizes = []
    for instr in ast:
        processed_ops = []
        for op in instr.ops:
            processed_ops.extend(op.untyped_repr(None))
        processed_ops.append(instr.uf)
        if instr.cond:
            name, _ = branch_ops[instr.name]
            processed_ops = [instr.cond] + processed_ops
        else:
            name = instr.name

        print processed_ops
        # print name
        (_, size) = encode(name.upper(), processed_ops)
        sizes.append(size)

    #print(sizes)

    # second pass uses sizes for labels, accumulates generated instructions
    values = []
    for instr in ast:
        processed_ops = []
        for op in instr.ops:
            processed_ops.extend(op.untyped_repr((labels, sizes)))
        processed_ops.append(instr.uf)
        if instr.cond:
            name, _ = branch_ops[instr.name]
            processed_ops = [instr.cond] + processed_ops
        else:
            name = instr.name
        # print name
        (value, _) = encode(name.upper(), processed_ops)
        values.append(value)

    # print(values)

    outputs = []
    for (value, size) in zip(values, sizes):
	nytes = []
	for i in range(size):
	    nyte = value >> (9*i)
            nyte = nyte & ((1<<9)-1)
	    nytes.append(nyte)
	nytes.reverse()
        outputs.append(nytes)
    return outputs

def tests():
    asm = '''
AD. r1, r3, r2
foo:
MUF r0, r5, r10
BLE &foo
HT
'''
    print(asm)
    ast, labels = parse(asm)
    print(labels)
    print(ast)
    print('\n'.join(map(str, ast)))
    assemble(ast, labels)

if __name__ == '__main__':
    if len(sys.argv) == 3:
        with open(sys.argv[1], 'r') as f:
            asm = f.read()
            ast, labels = parse(asm)
            print ast, labels
            output = assemble(ast, labels)
            print(output)
	with open(sys.argv[2], 'w') as f2:
	    ba_full = bitarray()
	    for ins in output:
		ba_temp = bitarray()
                for nyte in ins:    
	    	    ba = bitarray()
                    ba.frombytes(struct.pack('>H',nyte))
		    ba = ba[7:]
		    ba_temp += ba
            	ba2 = bitarray()
	    	ba2[0:9] = ba_temp[9:18]
	        ba2[9:18] = ba_temp[0:9]
	    	ba2[18:27] = ba_temp[18:27]
		ba_full += ba2
	    f2.write(ba_full.tobytes())
    else:
        tests()
