from assembler import *
from bits import *
from gen.parse_ini import CONSTS
from ins_class import *
from maps import *
from packers import *
import math
import sys
import pdb

def disassemble_bytes(bytes):
    nytes = bits2nytes(bytes2bits(bytes))
    return disassemble_nytes(nytes)

def disassemble_nytes(nytes):
    output = []
    while len(nytes) > 1:
        try:
            (op, (data, size)) = try_parse(nytes)
            #print "Got %r" % op
            tmp = swapendian(list(nytes[:size]))
            #print "# %r, %r, %r" % (op, nytes2bits(tmp), data)
            tmp = enc_fun_to_decprime[enc_op_to_fun[op]](op, data)
            output.append(tmp)
            #print output[-1]
            nytes = nytes[size:]
        except Exception as e:
            import traceback
            traceback.print_exc()
            #raise e
            return output
    return output

def try_parse(nytes):
    #print("try_parse")
    candidates = set()
    for enc in enc_fun_to_op:
        def compare(a, b):
            l = min(len(a), len(b))
            return a[-l:] == b[-l:]
        size = enc_fun_to_size[enc]
        nytescopy = swapendian(list(nytes[:size]))
        #print("  try_parse: %r" % nytes2bits(nytescopy))
        #print nytescopy
        #print nytes2bits(nytescopy)
        opcodes = set()
        opcode2s = set()
        has_opcode2 = False
        #print enc_fun_to_fields[enc]
        for (fieldname, start, end) in enc_fun_to_fields[enc]:
            tmp = nytes2bits(nytescopy)[start:end+1]
            #print "\ttmp %r" % tmp
            for op in enc_fun_to_op[enc]:
                if fieldname == 'opcode':
                    to_test = op_bits[op][0]
                    #print "\t\topcode %r" % ((op, to_test),)
                    if compare(to_test, tmp):
                        opcodes.add(op)
                if fieldname == 'opcode2':
                    has_opcode2 = True
                    to_test = op_bits[op][1]
                    #print "\t\topcode2 %r" % ((op, to_test),)
                    if compare(to_test, tmp):
                        opcode2s.add(op)
                if fieldname in CONSTS:
                    if bits2num(tmp) != CONSTS[fieldname]:
                        opcodes.discard(op)
                        opcode2s.discard(op)
        if has_opcode2:
            intersection = opcodes.intersection(opcode2s)
        else:
            intersection = opcodes
        #print "\t%r" % ((has_opcode2, intersection),)
        if len(intersection) == 1:
            the_size = size
        candidates = candidates.union(intersection)
    #print candidates
    if len(candidates) == 1:
        nytescopy = swapendian(list(nytes[:the_size]))
        op = list(candidates)[0]
        #print "; %r" % nytes2bits(nytescopy)
        return (op, dec_op_to_fun[op](nytes2num(nytescopy)))
    else:
        raise Exception("Non-unique or empty decode: %r" % (candidates,))

'''
def leftpad(bits, size):
    remainder = size - len(bits)
    if remainder >= 0:
        return ([0] * remainder) + bits
    else:
        return bits
'''

if __name__ == '__main__':
    if len(sys.argv) == 2:
        data = open(sys.argv[1], 'r').read()
        #print bytes2bits(data)
        tmp = disassemble_bytes(data)
        for thing in tmp:
            print thing
