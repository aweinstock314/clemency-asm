import assembler

def asm(asm):
    ast, labels = assembler.parse(asm)
    return assembler.assemble(ast, labels)
