#!/usr/bin/env python2
from ins_class import *
import re

class ParseException:
    def __init__(self, line, lineno, msg):
        self.line = line
        self.lineno = lineno
        self.msg = msg
    def __repr__(self):
        return 'ParseException on line %d: %s\n%r\n' % (self.lineno, self.msg, self.line)

class Instruction:
    def __init__(self, instr):
        self.instr = instr

LITERAL_REGEX = '(0b[01]+|0x[0-9a-fA-F]+|\d+)'
MEMORY_REGEX = r'^\[(r[0-9]+)\s*\+\s*'+LITERAL_REGEX+',\s*'+LITERAL_REGEX+'\]$' # TODO: hex/bin offsets?

class Assembler:
    def __init__(self, asm):
        self.lines = asm.split('\n')

    def parse(self):
        output = []
        labels = {}
        for i, line in enumerate(self.lines):
            line = line.split(';',1)[0].split('#',1)[0].strip() # comments
            match = re.match('^(\w+):\s*(.*)$', line)
            if match:
                label = match.group(1)
                labels[label] = len(output)
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
                for op in rest.split(','):
                    op = op.strip()
                    # number (hex/int/bin literals) | r[0-31] | PC | ST | RA
                    memory_match = re.match(MEMORY_REGEX, op)
                    if memory_match:
                        reg, offset, regcount = memory_match.groups()
                        offset, regcount = int(offset, 0), int(regcount, 0)
                        return Mem(reg, offset, regcount)
                    elif op in ['PC', 'ST', 'RA', 'FL']:
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
            output.append(Ins(name, uf, ops))
        return (output, labels)

def tests():
    a = Assembler('''
AD. r1, r3, r2
foo:
MUF r0, r5, r10
BLE &foo
HT
''')
    print(a.parse())

if __name__ == '__main__':
    tests()
