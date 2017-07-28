import assembler

def asm(asm):
    ast, labels = assembler.parse(asm)
    return assembler.assemble(ast, labels)

def assemble(asm):
    ast, labels = assembler.parse(asm)
    output = assembler.assemble(ast, labels)
    return assembler.binary_encode(output).tobytes()

