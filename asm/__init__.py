import assembler
import struct

def asm_bytes(asm):
    ast, labels = assembler.parse(asm)
    output = assembler.assemble(ast, labels)
    return assembler.binary_encode(output).tobytes()

def asm(asm):
    ast, labels = assembler.parse(asm)
    return assembler.assemble(ast, labels)
