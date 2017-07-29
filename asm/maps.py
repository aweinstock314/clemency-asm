from collections import defaultdict
from ins_class import *
from packers import *

enc_fun_to_op = {
    enc_ra_rb_me: ['SMP'], 
    enc_ra_rb_rc: ['AD', 'ADC', 'ADCM', 'ADF', 'ADFM', 'ADM', 'AN', 'ANM', 'DMT', 'DV', 'DVF', 'DVFM', 'DVM', 'DVS', 'DVSM', 'MD', 'MDF', 'MDFM', 'MDM', 'MDS', 'MDSM', 'MU', 'MUF', 'MUFM', 'MUM', 'MUS', 'MUSM', 'OR', 'ORM', 'RL', 'RLM', 'RR', 'RRM', 'SA', 'SAM', 'SB', 'SBC', 'SBCM', 'SBF', 'SBFM', 'SBM', 'SL', 'SLM', 'SR', 'SRM', 'XR', 'XRM'], 
    enc_no_re: ['DBRK', 'HT', 'IR', 'RE', 'WT'], 
    enc_co_ra: ['BR', 'CR'], 
    enc_ra_rb_lo_ve_no_fl: ['FTI', 'FTIM', 'ITF', 'ITFM'], 
    enc_ra_rb_of_re: ['LDS', 'LDT', 'LDW', 'STS', 'STT', 'STW'],
    enc_ra_rb_of_re_i: ['LDSI','LDTI','LDWI','STSI','STTI','STWI'],
    enc_ra_rb_of_re_d: ['LDSD','LDTD','LDWD','STSD','STTD','STWD'],
    enc_of: ['CAR'], 
    enc_ra_rb_lo_ve_no_fl_al: ['RMP'], 
    enc_ra_rb_lo_ve_no_fl_al_tw: ['ZES', 'ZEW', 'SES', 'SEW'],
    enc_ra_im_al: ['MH', 'ML', 'MS'], 
    enc_ra_rb_sh_ve: ['CM', 'CMF', 'CMFM', 'CMM'], 
    enc_ra_no_fl: ['DI', 'EI', 'RF', 'SF'], 
    enc_lo: ['BRA', 'BRR', 'CAA'], 
    enc_co: ['B', 'C'], 
    enc_ra_rb_lo_op: ['BF', 'BFM', 'NG', 'NGF', 'NGFM', 'NGM', 'NT', 'NTM'], 
    enc_ra_wi_fl: ['RND', 'RNDM'], 
    enc_ra_im: ['CMI', 'CMIM'], 
    enc_ra_rb_im: ['ADCI', 'ADCIM', 'ADI', 'ADIM', 'ANI', 'DVI', 'DVIM', 'DVIS', 'DVISM', 'MDI', 'MDIM', 'MDIS', 'MDISM', 'MUI', 'MUIM', 'MUIS', 'MUISM', 'ORI', 'RLI', 'RLIM', 'RRI', 'RRIM', 'SAI', 'SAIM', 'SBCI', 'SBCIM', 'SBI', 'SBIM', 'SLI', 'SLIM', 'SRI', 'SRIM', 'XRI'],
}

enc_fun_to_decprime = {
    enc_ra_rb_me: lambda op, (_, _1, ra, rb, me, uf): Ins(op, uf, [Reg(ra), Reg(rb), MemoryFlags(me)]),
    enc_ra_rb_rc: lambda op, (_, _1, ra, rb, rc, uf): Ins(op, uf, [Reg(ra), Reg(rb), Reg(rc)]),
    enc_no_re: lambda op, (_, uf): Ins(op, uf, []),
    enc_co_ra: lambda op, (_, _1, co, ra, uf): Ins(inv_branch_ops[(op.lower(), co)], uf, [Reg(ra)]),
    enc_ra_rb_lo_ve_no_fl: lambda op, (_, _1, ra, rb, uf): Ins(op, uf, [Reg(ra), Reg(rb)]),
    enc_ra_rb_of_re: lambda op, (_, _1, ra, rb, mem, regcount, uf): Ins(op, uf, [Reg(ra), Mem(rb, mem, regcount)]),
    enc_ra_rb_of_re_i: lambda op, (_, _1, ra, rb, mem, regcount, uf): Ins(op, uf, [Reg(ra), Mem(rb, mem, regcount)]),
    enc_ra_rb_of_re_d: lambda op, (_, _1, ra, rb, mem, regcount, uf): Ins(op, uf, [Reg(ra), Mem(rb, mem, regcount)]),
    enc_of: lambda op, (_, of, uf): Ins(op, uf, [Imm(of)]),
    enc_ra_rb_lo_ve_no_fl_al: lambda op, (_, _1, ra, rb, uf): Ins(op, uf, [Reg(ra), Reg(rb)]),
    enc_ra_rb_lo_ve_no_fl_al_tw: lambda op, (_, _1, ra, rb, uf): Ins(op, uf, [Reg(ra), Reg(rb)]),
    enc_ra_im_al: lambda op, (_, ra, im, uf): Ins(op, uf, [Reg(ra), Imm(im)]),
    enc_ra_rb_sh_ve: lambda op, (_, ra, rb, uf): Ins(op, uf, [Reg(ra), Reg(rb)]),
    enc_ra_no_fl: lambda op, (_, _1, ra, uf): Ins(op, uf, [Reg(ra)]),
    enc_lo: lambda op, (_, lo, uf): Ins(op, uf, [Imm(lo)]),
    enc_co: lambda op, (_, co, of, uf): Ins(inv_branch_ops[(op.lower(), co)], uf, [Imm(of)]),
    enc_ra_rb_lo_op: lambda op, (_, _1, ra, rb, uf): Ins(op, uf, [Reg(ra), Reg(rb)]),
    enc_ra_wi_fl: lambda op, (_, _1, ra, uf): Ins(op, uf, [Reg(ra)]),
    enc_ra_im: lambda op, (_, ra, im, uf): Ins(op, uf, [Reg(ra), Imm(im)]),
    enc_ra_rb_im: lambda op, (_, _1, ra, rb, im, uf): Ins(op, uf, [Reg(ra), Reg(rb), Imm(im)]),
}

enc_op_to_fun = {}
for fun, ops in enc_fun_to_op.items():
    for op in ops:
        enc_op_to_fun[op] = fun

dec_fun_to_op = {enc_fun_to_dec_fun[enc]: enc_fun_to_op[enc] for enc in enc_fun_to_op}

dec_op_to_fun = {}
for fun, ops in dec_fun_to_op.items():
    for op in ops:
        dec_op_to_fun[op] = fun

op_bits = {
    'AD':[0b000000,0b0000],
    'ADC':[0b0100000,0b0000],
    'ADCI':[0b0100000,0b01],
    'ADCIM':[0b0100010,0b01],
    'ADCM':[0b0100010,0b0000],
    'ADF':[0b0000001,0b0000],
    'ADFM':[0b0000011,0b0000],
    'ADI':[0b0000000,0b01],
    'ADIM':[0b0000010,0b01],
    'ADM':[0b0000010,0b0000],
    'AN': [0b0010100,0b0000],
    'ANI':[0b0010100,0b01],
    'ANM':[0b0010110,0b0000],
    'B':[0b110000],
    'BF':[0b101001100,0b1000000],
    'BFM':[0b101001110,0b1000000],
    'BR':[0b110010, 0b000],
    'BRA':[0b111000100],
    'BRR':[0b111000000],
    'C':[0b110101],
    'CAA':[0b111001100], 
    'CAR':[0b111001000], 
    'CM':[0b10111000], 
    'CMF':[0b10111010], 
    'CMFM':[0b10111110], 
    'CMI':[0b10111001], 
    'CMIM':[0b10111101], 
    'CMM':[0b10111100], 
    'CR':[0b110111,0b000], 
    'DBRK':[0b111111111111111111], 
    'DI':[0b101000000101,0b0], 
    'DMT':[0b0110100,0b00000], 
    'DV':[0b0001100,0b0000], 
    'DVF':[0b0001101,0b0000], 
    'DVFM':[0b0001111,0b0000], 
    'DVI':[0b0001100,0b01], 
    'DVIM':[0b0001110,0b01], 
    'DVIS':[0b0001100,0b11],
    'DVISM':[0b0001110,0b11], 
    'DVM':[0b0001110,0b0000], 
    'DVS':[0b0001100,0b0010], 
    'DVSM':[0b0001110,0b0010], 
    'EI':[0b101000000100,0b0], 
    'FTI':[0b101000101,0b00000000], 
    'FTIM':[0b101000111,0b00000000], 
    'HT':[0b101000000011000000], 
    'IR':[0b101000000001000000], 
    'ITF':[0b101000100,0b00000000], 
    'ITFM':[0b101000110,0b00000000], 
    'LDS':[0b1010100,0b000], 
    'LDSI':[0b1010100,0b000], 
    'LDSD':[0b1010100,0b000], 
    'LDT':[0b1010110,0b000],
    'LDTI':[0b1010110,0b000],
    'LDTD':[0b1010110,0b000],
    'LDW':[0b1010101,0b000], 
    'LDWI':[0b1010101,0b000], 
    'LDWD':[0b1010101,0b000], 
    'MD':[0b0010000,0b0000], 
    'MDF':[0b0010001,0b0000], 
    'MDFM':[0b0010011,0b0000], 
    'MDI':[0b0010000,0b01], 
    'MDIM':[0b0010010,0b01], 
    'MDIS':[0b0010000,0b11], 
    'MDISM':[0b0010010,0b11], 
    'MDM':[0b0010010,0b0000], 
    'MDS':[0b0010000,0b0010], 
    'MDSM':[0b0010010,0b0010], 
    'MH':[0b10001], 
    'ML':[0b10010], 
    'MS':[0b10011], 
    'MU':[0b0001000,0b0000], 
    'MUF':[0b0001001,0b0000], 
    'MUFM':[0b0001011,0b0000], 
    'MUI':[0b0001000,0b01], 
    'MUIM':[0b0001010,0b01], 
    'MUIS':[0b0001000,0b11], 
    'MUISM':[0b0001010,0b11], 
    'MUM':[0b0001010,0b0000], 
    'MUS':[0b0001000,0b0010], 
    'MUSM':[0b0001010,0b0010],
    'NG':[0b101001100,0b0000000],
    'NGF':[0b101001101,0b0000000],
    'NGFM':[0b101001111,0b0000000],
    'NGM':[0b101001110,0b0000000],
    'NT':[0b101001100,0b0100000],
    'NTM':[0b101001110,0b0100000],
    'OR':[0b0011000,0b0000],
    'ORI':[0b0011000,0b01],
    'ORM':[0b0011010,0b0000],
    'RE':[0b101000000000000000],
    'RF':[0b101000001100,0b0],
    'RL':[0b0110000,0b0000],
    'RLI':[0b1000000,0b00],
    'RLIM':[0b1000010,0b00],
    'RLM':[0b0110010,0b0000], 
    'RMP':[0b1010010,0b0000000000],
    'RND':[0b101001100,0b000001100000],
    'RNDM':[0b101001110,0b000001100000],
    'RR':[0b0110001,0b0000],
    'RRI':[0b1000001,0b00],
    'RRIM':[0b1000011,0b00], 
    'RRM':[0b0110011,0b0000], 
    'SA':[0b0101101,0b0000], 
    'SAI':[0b0111101,0b00], 
    'SAIM':[0b0111111,0b00], 
    'SAM':[0b0101111,0b0000], 
    'SB':[0b0000100,0b0000], 
    'SBC':[0b0100100,0b0000], 
    'SBCI':[0b0100100,0b01], 
    'SBCIM':[0b0100110,0b01], 
    'SBCM':[0b0100110,0b0000], 
    'SBF':[0b0000101,0b0000], 
    'SBFM':[0b0000111,0b0000],
    'SBI':[0b0000100,0b01], 
    'SBIM':[0b0000110,0b01], 
    'SBM':[0b0000110,0b0000], 
    'SES':[0b101000000111,0b00000], 
    'SEW':[0b101000001000,0b00000], 
    'SF':[0b101000001011,0b0], 
    'SL':[0b0101000,0b0000], 
    'SLI':[0b0111000,0b00], 
    'SLIM':[0b0111010,0b00], 
    'SLM':[0b0101010,0b0000], 
    'SMP':[0b1010010,0b0000000], 
    'SR':[0b0101001,0b0000], 
    'SRI':[0b0111001,0b00], 
    'SRIM':[0b0111011,0b00], 
    'SRM':[0b0101011,0b0000], 
    'STS':[0b1011000,0b00], 
    'STSI':[0b1011000,0b00], 
    'STSD':[0b1011000,0b00], 
    'STT':[0b1011010,0b000], 
    'STTI':[0b1011010,0b000], 
    'STTD':[0b1011010,0b000], 
    'STW':[0b1011001,0b000], 
    'STWI':[0b1011001,0b000], 
    'STWD':[0b1011001,0b000], 
    'WT':[0b101000000010000000], 
    'XR':[0b0011100,0b0000], 
    'XRI':[0b0011100,0b01], 
    'XRM':[0b0011110,0b0000], 
    'ZES':[0b101000001001, 0b00000], 
    'ZEW':[0b101000001010,0b00000],
}

'''
bigint_endian_inverse = lambda x: int(bin(x)[2:][::-1], 2) #wrong (leading zeros)
bitop_le = {op: tuple(map(bigint_endian_inverse, bits)) for op, bits in op_bits.items()}
inv_bitop_le = {}
for k, v in bitop_le.items():
    inv_bitop_le[v] = inv_bitop_le.get(v, [])
    inv_bitop_le[v].append(k)
'''

op_fields = {op: enc_fun_to_fields[enc_op_to_fun[op]] for op in op_bits}

bits_to_op = defaultdict(dict)
for op, bits in op_bits.items():
    b1, b2 = bits[0], 0
    if len(bits) >= 2:
        b2 = bits[1]
    bits_to_op[b1][b2] = op
