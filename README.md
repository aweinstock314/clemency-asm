# asm
Python cLEMENCy asm lib

## Using the assembler

```
$ cat hello.clem
; both semicolon and sharp can be used as comments
# relative jumps/calls to labels work (labels can also be used as immediates, they're always instruction-relative)
b &postobfuscation
# the {db, dw, dt} pseudo-ops embed immediate data at the current assembly point, and can be used to create impossible disassemblies
dt 0x68, 0x65, 0x6c
dw 0x6c, 0x6f
postobfuscation:
ml r0, 0
; The disassembler module has helper functions for packing bytes (TODO: move to better module?)
#>>> from disassembler import *
#>>> bits2nytes(bytes2bits("hello"))
#[208, 405, 355, 198, 480]
ml r1, 208
ml r2, 405
ml r3, 355
ml r4, 198
ml r5, 480
# 0x5010000 is the magic address for IO buffering
sts r1, [r0 + 0x5010000, 5]
ml r1, 5
# writes to 0x5012000 are treated as a size to the 0x5010000 buffer, and cause it to be flushed to output
sts r1, [r0 + 0x5012000, 1]
ht
$ python asm/assembler.py hello.clem hello.out
$ ./clemency-emu -d 0 hello.out
No map file found
Loading hello.out
R00: 0000000    R01: 0000000    R02: 0000000    R03: 0000000
R04: 0000000    R05: 0000000    R06: 0000000    R07: 0000000
R08: 0000000    R09: 0000000    R10: 0000000    R11: 0000000
R12: 0000000    R13: 0000000    R14: 0000000    R15: 0000000
R16: 0000000    R17: 0000000    R18: 0000000    R19: 0000000
R20: 0000000    R21: 0000000    R22: 0000000    R23: 0000000
R24: 0000000    R25: 0000000    R26: 0000000    R27: 0000000
R28: 0000000     ST: 0000000     RA: 0000000     PC: 0000000
 FL: 0000000

0000000:                         61e0008         b      +0x8 (0x0000008)
> u 0
0000000:                         61e0008         b      +0x8 (0x0000008)
0000003: Disassembly Error
> u 8
0000008:                         4800000         ml     R00, 0x0
000000b:                         48200d0         ml     R01, 0xd0
000000e:                         4840195         ml     R02, 0x195
0000011:                         4860163         ml     R03, 0x163
0000014:                         48800c6         ml     R04, 0xc6
0000017:                         48a01e0         ml     R05, 0x1e0
000001a:                         2c040428080000  sts    R01, [R00 - 0x2ff0000, 5]
0000020:                         4820005         ml     R01, 0x5
0000023:                         2c040028090000  sts    R01, [R00 - 0x2fee000]
0000029:                         280c0           ht
000002b:                         0000000         ad     R00, R00, R00
000002e:                         0000000         ad     R00, R00, R00
0000031:                         0000000         ad     R00, R00, R00
0000034:                         0000000         ad     R00, R00, R00
0000037:                         0000000         ad     R00, R00, R00
000003a:                         0000000         ad     R00, R00, R00
000003d:                         0000000         ad     R00, R00, R00
0000040:                         0000000         ad     R00, R00, R00
0000043:                         0000000         ad     R00, R00, R00
0000046:                         0000000         ad     R00, R00, R00
> g
helloHT instruction encountered at 0000029
Connected IP: 0.0.0.0
CPU no longer running
Total instructions: 11, 0.0000m instructions/sec
Running time: 19.906709 seconds, sleep time: 0.000000 seconds
```

## Stability/correctness tests

`corpus.py` generates a cartesian product of all opcodes with a few different immediates.
`disassemble(assemble(corpus)) == corpus` is verified by `test.sh`:

```
$ cat test.sh
#!/bin/sh
echo "Generating corpus"
time python asm/corpus.py > corpus.clem
echo "Assembling corpus"
time python asm/assembler.py corpus.clem corpus.out
echo "Disassembling corpus"
time python asm/disassembler.py corpus.out > corpus2.clem

echo "Length of the diff:"
diff corpus.clem corpus2.clem | wc
$ bash test.sh
Generating corpus

real	0m0.090s
user	0m0.076s
sys	0m0.012s
Assembling corpus

real	0m0.832s
user	0m0.816s
sys	0m0.016s
Disassembling corpus

real	0m14.144s
user	0m14.140s
sys	0m0.012s
Length of the diff:
      0       0       0
```
