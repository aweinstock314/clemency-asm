from ins_class import *
from maps import *
from packers import *
from assembler import *
from gen.parse_ini import CONSTS
import math
import struct
import sys
import pdb

def disassemble(bytes):
    nytes = bits2nytes(bytes2bits(bytes))
    output = []
    while len(nytes) > 0:
        (op, (data, size)) = try_parse(nytes)
        #print "Got %r" % op
        tmp = enc_fun_to_decprime[enc_op_to_fun[op]](op, data)
        output.append(tmp)
        print output[-1]
        nytes = nytes[size:]
    return output

def try_parse(nytes):
    #print("try_parse")
    candidates = set()
    for enc in enc_fun_to_op:
        size = enc_fun_to_size[enc]
        nytescopy = list(nytes[:size])
        swapendian(nytescopy)
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
                    to_test = list(reversed(num2bits(op_bits[op][0])))
                    #print "\t\topcode %r" % ((op, to_test),)
                    if leftpad(to_test, len(tmp)) == tmp:
                        opcodes.add(op)
                if fieldname == 'opcode2':
                    has_opcode2 = True
                    to_test = list(reversed(num2bits(op_bits[op][1])))
                    #print "\t\topcode2 %r" % ((op, to_test),)
                    if leftpad(to_test, len(tmp)) == tmp:
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
        candidates = candidates.union(intersection)
    #print candidates
    if len(candidates) == 1:
        op = list(candidates)[0]
        return (op, dec_op_to_fun[op](nytes2num(nytescopy)))
    else:
        raise Exception("Non-unique or empty decode: %r" % (candidates,))


def bytes2bits(bytes):
    output = []
    for byte in bytes:
        b = struct.unpack("B", byte)[0]
        for i in range(8):
            output.append((b >> (7-i)) & 1)
    return output

def bits2nytes(bits):
    ret = []
    for i in range(0, len(bits), 9):
        tmp = 0
        for j in range(9):
            if i+j < len(bits):
                tmp += bits[i+j] << j
        ret.append(tmp)
    return ret

def bits2num(bits):
    ret = 0
    for (i, b) in enumerate(bits):
        ret += b << i
    return ret

def num2bits(num):
    output = []
    while num > 0:
        output.append(num & 1)
        num >>= 1
    if len(output) == 0:
        output = [0]
    return output

def nytes2bits(nytes):
    output = []
    for nyte in nytes:
        for i in range(9):
            output.append((nyte >> i) & 1)
    return output

for i in range(0,2**10):
    '''
    print 'i', i
    print 'bits', num2bits(i)
    print 'nytes', bits2nytes(num2bits(i))
    print 'bits', nytes2bits(bits2nytes(num2bits(i)))
    print 'converted i', bits2num(nytes2bits(bits2nytes(num2bits(i))))
    '''
    assert bits2num(num2bits(i)) == i
    assert bits2num(nytes2bits(bits2nytes(num2bits(i)))) == i
    #assert bits2num(bytes2bits(bits2bytes(num2bits(i)))) == i

def nytes2num(nytes):
    return bits2num(nytes2bits(nytes))

def leftpad(bits, size):
    remainder = size - len(bits)
    if remainder >= 0:
        return ([0] * remainder) + bits
    else:
        return bits

if __name__ == '__main__':
    if len(sys.argv) == 2:
        data = open(sys.argv[1], 'r').read()
        #print bytes2bits(data)
        tmp = disassemble(data)
        for thing in tmp:
            print thing
