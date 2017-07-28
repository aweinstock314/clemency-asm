import assembler
import struct

def assemble(asm):
    ast, labels = assembler.parse(asm)
    output = assembler.assemble(ast, labels)
    return assembler.binary_encode(output).tobytes()

def asm(asm):
    ast, labels = assembler.parse(asm)
    output = assembler.assemble(ast, labels)
    enc = assembler.binary_encode(output).tobytes()
    print enc
    byte_list = []
    for char in enc:
	byte_list.append(struct.unpack('>B', char)[0])
    return byte_list   
