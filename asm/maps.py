from collections import defaultdict
from packers import *

enc_fun_to_op = {
    enc_ra_rb: ['ZES', 'ZEW', 'SES', 'SEW'],
    enc_ra_rb_me: ['SMP'], 
    enc_ra_rb_rc: ['AD', 'ADC', 'ADCM', 'ADF', 'ADFM', 'ADM', 'AN', 'ANM', 'DMT', 'DV', 'DVF', 'DVFM', 'DVM', 'DVS', 'DVSM', 'MD', 'MDF', 'MDFM', 'MDM', 'MDS', 'MDSM', 'MU', 'MUF', 'MUFM', 'MUM', 'MUS', 'MUSM', 'OR', 'ORM', 'RL', 'RLM', 'RR', 'RRM', 'SA', 'SAM', 'SB', 'SBC', 'SBCM', 'SBF', 'SBFM', 'SBM', 'SL', 'SLM', 'SR', 'SRM', 'XR', 'XRM'], 
    enc_no_re: ['DBRK', 'HT', 'IR', 'RE', 'WT'], 
    enc_co_ra: ['BR', 'CR'], 
    enc_ra_rb_lo_ve_no_fl: ['FTI', 'FTIM', 'ITF', 'ITFM'], 
    enc_ra_rb_of_re: ['LDS', 'LDT', 'LDW', 'STS', 'STT', 'STW'],
    enc_ra_rb_of_re_i: ['LDSI','LDTI','LDWI','STSI','STTI','STWI'],
    enc_ra_rb_of_re_d: ['LDSD','LDTD','LDWD','STSD','STTD','STWI'],
    enc_of: ['CAR'], 
    enc_ra_rb_lo_ve_no_fl_al: ['RMP'], 
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

enc_op_to_fun = {}
for fun, ops in enc_fun_to_op.items():
    for op in ops:
        enc_op_to_fun[op] = fun

dec_fun_to_op = {
    dec_ra_rb_me: ['SMP'], 
    dec_ra_rb_rc: ['AD', 'ADC', 'ADCM', 'ADF', 'ADFM', 'ADM', 'AN', 'ANM', 'DMT', 'DV', 'DVF', 'DVFM', 'DVM', 'DVS', 'DVSM', 'MD', 'MDF', 'MDFM', 'MDM', 'MDS', 'MDSM', 'MU', 'MUF', 'MUFM', 'MUM', 'MUS', 'MUSM', 'OR', 'ORM', 'RL', 'RLM', 'RR', 'RRM', 'SA', 'SAM', 'SB', 'SBC', 'SBCM', 'SBF', 'SBFM', 'SBM', 'SL', 'SLM', 'SR', 'SRM', 'XR', 'XRM'], 
    dec_no_re: ['DBRK', 'HT', 'IR', 'RE', 'WT'], 
    dec_co_ra: ['BR', 'CR'], 
    dec_ra_rb_lo_ve_no_fl: ['FTI', 'FTIM', 'ITF', 'ITFM'], 
    dec_ra_rb_of_re: ['LDS', 'LDT', 'LDW', 'STS', 'STT', 'STW'], 
    dec_of: ['CAR'], 
    dec_ra_rb_lo_ve_no_fl_al: ['RMP', 'SES', 'SEW', 'ZES', 'ZEW'], 
    dec_ra_im_al: ['MH', 'ML', 'MS'], 
    dec_ra_rb_sh_ve: ['CM', 'CMF', 'CMFM', 'CMM'], 
    dec_ra_no_fl: ['DI', 'EI', 'RF', 'SF'], 
    dec_lo: ['BRA', 'BRR', 'CAA'], 
    dec_co: ['B', 'C'], 
    dec_ra_rb_lo_op: ['BF', 'BFM', 'NG', 'NGF', 'NGFM', 'NGM', 'NT', 'NTM'], 
    dec_ra_wi_fl: ['RND', 'RNDM'], 
    dec_ra_im: ['CMI', 'CMIM'], 
    dec_ra_rb_im: ['ADCI', 'ADCIM', 'ADI', 'ADIM', 'ANI', 'DVI', 'DVIM', 'DVIS', 'DVISM', 'MDI', 'MDIM', 'MDIS', 'MDISM', 'MUI', 'MUIM', 'MUIS', 'MUISM', 'ORI', 'RLI', 'RLIM', 'RRI', 'RRIM', 'SAI', 'SAIM', 'SBCI', 'SBCIM', 'SBI', 'SBIM', 'SLI', 'SLIM', 'SRI', 'SRIM', 'XRI'],
}

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
    'LDW':[0b1010101,0b000], 
    'LDWI':[0b1010101,0b000], 
    'LDWD':[0b1010101,0b000], 
    'MD':[0b0010000,0b0000], 
    'MDF':[0b0010001,0b0000], 
    'MDFM':[0b0010011,0b0000], 
    'MDI':[0b0010000,0b10], 
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

bits_to_op = {'110000': ['B', <function enc_co at 0x7fec5c855758>], '101001111': {'0000000': ['NGFM', <function enc_ra_rb_lo_op at 0x7fec5c848d70>]}, '101000100': {'00000000': ['ITF', <function enc_ra_rb_lo_ve_no_fl at 0x7fec5c848f50>]}, '101000101': {'00000000': ['FTI', <function enc_ra_rb_lo_ve_no_fl at 0x7fec5c848f50>]}, '0001011': {'0000': ['MUFM', <function enc_ra_rb_rc at 0x7fec5c848b90>]}, '0001010': {'11': ['MUISM', <function enc_ra_rb_im at 0x7fec5c848c80>], '01': ['MUIM', <function enc_ra_rb_im at 0x7fec5c848c80>], '0000': ['MUM', <function enc_ra_rb_rc at 0x7fec5c848b90>], '0010': ['MUSM', <function enc_ra_rb_rc at 0x7fec5c848b90>]}, '101001110': {'000001100000': ['RNDM', <function enc_ra_wi_fl at 0x7fec5c855668>], '0100000': ['NTM', <function enc_ra_rb_lo_op at 0x7fec5c848d70>], '1000000': ['BFM', <function enc_ra_rb_lo_op at 0x7fec5c848d70>], '0000000': ['NGM', <function enc_ra_rb_lo_op at 0x7fec5c848d70>]}, '111000100': ['BRA', <function enc_lo at 0x7fec5c855848>], '10111000': ['CM', <function enc_ra_rb_sh_ve at 0x7fec5c855140>], '10111001': ['CMI', <function enc_ra_im at 0x7fec5c8552a8>], '101000001001': {'00000': ['ZES', <function enc_ra_rb_lo_ve_no_fl_al at 0x7fec5c8550c8>]}, '110010': {'000': ['BR', <function enc_co_ra at 0x7fec5c855488>]}, '0001000': {'11': ['MUIS', <function enc_ra_rb_im at 0x7fec5c848c80>], '01': ['MUI', <function enc_ra_rb_im at 0x7fec5c848c80>], '0000': ['MU', <function enc_ra_rb_rc at 0x7fec5c848b90>], '0010': ['MUS', <function enc_ra_rb_rc at 0x7fec5c848b90>]}, '0001001': {'0000': ['MUF', <function enc_ra_rb_rc at 0x7fec5c848b90>]}, '10111010': ['CMF', <function enc_ra_rb_sh_ve at 0x7fec5c855140>], '0100100': {'01': ['SBCI', <function enc_ra_rb_im at 0x7fec5c848c80>], '0000': ['SBC', <function enc_ra_rb_rc at 0x7fec5c848b90>]}, '0111101': {'00': ['SAI', <function enc_ra_rb_im at 0x7fec5c848c80>]}, '0101111': {'0000': ['SAM', <function enc_ra_rb_rc at 0x7fec5c848b90>]}, '0010011': {'0000': ['MDFM', <function enc_ra_rb_rc at 0x7fec5c848b90>]}, '0010010': {'11': ['MDISM', <function enc_ra_rb_im at 0x7fec5c848c80>], '01': ['MDIM', <function enc_ra_rb_im at 0x7fec5c848c80>], '0000': ['MDM', <function enc_ra_rb_rc at 0x7fec5c848b90>], '0010': ['MDSM', <function enc_ra_rb_rc at 0x7fec5c848b90>]}, '111001100': ['CAA', <function enc_lo at 0x7fec5c855848>], '101000000010000000': ['WT', <function enc_no_re at 0x7fec5c855a28>], '0101101': {'0000': ['SA', <function enc_ra_rb_rc at 0x7fec5c848b90>]}, '101000000011000000': ['HT', <function enc_no_re at 0x7fec5c855a28>], '1010110': {'000': ['LDT', <function enc_ra_rb_of_re at 0x7fec5c8489b0>]}, '0100110': {'01': ['SBCIM', <function enc_ra_rb_im at 0x7fec5c848c80>], '0000': ['SBCM', <function enc_ra_rb_rc at 0x7fec5c848b90>]}, '0111111': {'00': ['SAIM', <function enc_ra_rb_im at 0x7fec5c848c80>]}, '0010000': {'11': ['MDIS', <function enc_ra_rb_im at 0x7fec5c848c80>], '10': ['MDI', <function enc_ra_rb_im at 0x7fec5c848c80>], '0000': ['MD', <function enc_ra_rb_rc at 0x7fec5c848b90>], '0010': ['MDS', <function enc_ra_rb_rc at 0x7fec5c848b90>]}, '0010001': {'0000': ['MDF', <function enc_ra_rb_rc at 0x7fec5c848b90>]}, '0000101': {'0000': ['SBF', <function enc_ra_rb_rc at 0x7fec5c848b90>]}, '0110100': {'00000': ['DMT', <function enc_ra_rb_rc at 0x7fec5c848b90>]}, '0001101': {'0000': ['DVF', <function enc_ra_rb_rc at 0x7fec5c848b90>]}, '0001100': {'11': ['DVIS', <function enc_ra_rb_im at 0x7fec5c848c80>], '01': ['DVI', <function enc_ra_rb_im at 0x7fec5c848c80>], '0000': ['DV', <function enc_ra_rb_rc at 0x7fec5c848b90>], '0010': ['DVS', <function enc_ra_rb_rc at 0x7fec5c848b90>]}, '1010100': {'000': ['LDS', <function enc_ra_rb_of_re at 0x7fec5c8489b0>]}, '1010101': {'000': ['LDW', <function enc_ra_rb_of_re at 0x7fec5c8489b0>]}, '0011110': {'0000': ['XRM', <function enc_ra_rb_rc at 0x7fec5c848b90>]}, '0000111': {'0000': ['SBFM', <function enc_ra_rb_rc at 0x7fec5c848b90>]}, '0000110': {'01': ['SBIM', <function enc_ra_rb_im at 0x7fec5c848c80>], '0000': ['SBM', <function enc_ra_rb_rc at 0x7fec5c848b90>]}, '101000001100': {'0': ['RF', <function enc_ra_no_fl at 0x7fec5c855578>]}, '0100010': {'01': ['ADCIM', <function enc_ra_rb_im at 0x7fec5c848c80>], '0000': ['ADCM', <function enc_ra_rb_rc at 0x7fec5c848b90>]}, '101000000000000000': ['RE', <function enc_no_re at 0x7fec5c855a28>], '101000000111': {'00000': ['SES', <function enc_ra_rb_lo_ve_no_fl_al at 0x7fec5c8550c8>]}, '1011000': {'00': ['STS', <function enc_ra_rb_of_re at 0x7fec5c8489b0>]}, '0000011': {'0000': ['ADFM', <function enc_ra_rb_rc at 0x7fec5c848b90>]}, '0001110': {'11': ['DVISM', <function enc_ra_rb_im at 0x7fec5c848c80>], '01': ['DVIM', <function enc_ra_rb_im at 0x7fec5c848c80>], '0000': ['DVM', <function enc_ra_rb_rc at 0x7fec5c848b90>], '0010': ['DVSM', <function enc_ra_rb_rc at 0x7fec5c848b90>]}, '0001111': {'0000': ['DVFM', <function enc_ra_rb_rc at 0x7fec5c848b90>]}, '0011100': {'01': ['XRI', <function enc_ra_rb_im at 0x7fec5c848c80>], '0000': ['XR', <function enc_ra_rb_rc at 0x7fec5c848b90>]}, '111001000': ['CAR', <function enc_lo at 0x7fec5c855848>], '0000100': {'01': ['SBI', <function enc_ra_rb_im at 0x7fec5c848c80>], '0000': ['SB', <function enc_ra_rb_rc at 0x7fec5c848b90>]}, '10001': ['MH', <function enc_ra_im_al at 0x7fec5c855398>], '101000000001000000': ['IR', <function enc_no_re at 0x7fec5c855a28>], '0100000': {'01': ['ADCI', <function enc_ra_rb_im at 0x7fec5c848c80>], '0000': ['ADC', <function enc_ra_rb_rc at 0x7fec5c848b90>]}, '101000000101': {'0': ['DI', <function enc_ra_no_fl at 0x7fec5c855578>]}, '101000000100': {'0': ['EI', <function enc_ra_no_fl at 0x7fec5c855578>]}, '0101001': {'0000': ['SR', <function enc_ra_rb_rc at 0x7fec5c848b90>]}, '0101000': {'0000': ['SL', <function enc_ra_rb_rc at 0x7fec5c848b90>]}, '0110001': {'0000': ['RR', <function enc_ra_rb_rc at 0x7fec5c848b90>]}, '0110000': {'0000': ['RL', <function enc_ra_rb_rc at 0x7fec5c848b90>]}, '0010100': {'01': ['ANI', <function enc_ra_rb_im at 0x7fec5c848c80>], '0000': ['AN', <function enc_ra_rb_rc at 0x7fec5c848b90>]}, '110111': {'000': ['CR', <function enc_co_ra at 0x7fec5c855488>]}, '10011': ['MS', <function enc_ra_im_al at 0x7fec5c855398>], '10010': ['ML', <function enc_ra_im_al at 0x7fec5c855398>], '10111110': ['CMFM', <function enc_ra_rb_sh_ve at 0x7fec5c855140>], '1000011': {'00': ['RRIM', <function enc_ra_rb_im at 0x7fec5c848c80>]}, '1000010': {'00': ['RLIM', <function enc_ra_rb_im at 0x7fec5c848c80>]}, '1010000010000': {'00000': ['SEW', <function enc_ra_rb_lo_ve_no_fl_al at 0x7fec5c8550c8>]}, '0101010': {'0000': ['SLM', <function enc_ra_rb_rc at 0x7fec5c848b90>]}, '0101011': {'0000': ['SRM', <function enc_ra_rb_rc at 0x7fec5c848b90>]}, '0110010': {'0000': ['RLM', <function enc_ra_rb_rc at 0x7fec5c848b90>]}, '0110011': {'0000': ['RRM', <function enc_ra_rb_rc at 0x7fec5c848b90>]}, '0010110': {'0000': ['ANM', <function enc_ra_rb_rc at 0x7fec5c848b90>]}, '0011000': {'01': ['ORI', <function enc_ra_rb_im at 0x7fec5c848c80>], '0000': ['OR', <function enc_ra_rb_rc at 0x7fec5c848b90>]}, '0000001': {'0000': ['ADF', <function enc_ra_rb_rc at 0x7fec5c848b90>]}, '0000000': {'01': ['ADI', <function enc_ra_rb_im at 0x7fec5c848c80>]}, '110101': ['C', <function enc_co at 0x7fec5c855758>], '111000000': ['BRR', <function enc_lo at 0x7fec5c855848>], '1011010': {'000': ['STT', <function enc_ra_rb_of_re at 0x7fec5c8489b0>]}, '1010010': {'0000000000': ['RMP', <function enc_ra_rb_lo_ve_no_fl_al at 0x7fec5c8550c8>], '0000000': ['SMP', <function enc_ra_rb_me at 0x7fec5c848e60>]}, '10111101': ['CMIM', <function enc_ra_im at 0x7fec5c8552a8>], '10111100': ['CMM', <function enc_ra_rb_sh_ve at 0x7fec5c855140>], '111111111111111111': ['DBRK', <function enc_no_re at 0x7fec5c855a28>], '0111011': {'00': ['SRIM', <function enc_ra_rb_im at 0x7fec5c848c80>]}, '0111010': {'00': ['SLIM', <function enc_ra_rb_im at 0x7fec5c848c80>]}, '1000000': {'00': ['RLI', <function enc_ra_rb_im at 0x7fec5c848c80>]}, '1000001': {'00': ['RRI', <function enc_ra_rb_im at 0x7fec5c848c80>]}, '101001101': {'0000000': ['NGF', <function enc_ra_rb_lo_op at 0x7fec5c848d70>]}, '101001100': {'000001100000': ['RND', <function enc_ra_wi_fl at 0x7fec5c855668>], '0100000': ['NT', <function enc_ra_rb_lo_op at 0x7fec5c848d70>], '1000000': ['BF', <function enc_ra_rb_lo_op at 0x7fec5c848d70>], '0000000': ['NG', <function enc_ra_rb_lo_op at 0x7fec5c848d70>]}, '0011010': {'0000': ['ORM', <function enc_ra_rb_rc at 0x7fec5c848b90>]}, '0000010': {'01': ['ADIM', <function enc_ra_rb_im at 0x7fec5c848c80>], '0000': ['ADM', <function enc_ra_rb_rc at 0x7fec5c848b90>]}, '1011001': {'000': ['STW', <function enc_ra_rb_of_re at 0x7fec5c8489b0>]}, '101000111': {'00000000': ['FTIM', <function enc_ra_rb_lo_ve_no_fl at 0x7fec5c848f50>]}, '101000110': {'00000000': ['ITFM', <function enc_ra_rb_lo_ve_no_fl at 0x7fec5c848f50>]}, '000000': {'0000': ['AD', <function enc_ra_rb_rc at 0x7fec5c848b90>]}, '0111000': {'00': ['SLI', <function enc_ra_rb_im at 0x7fec5c848c80>]}, '0111001': {'00': ['SRI', <function enc_ra_rb_im at 0x7fec5c848c80>]}, '101000001010': {'00000': ['ZEW', <function enc_ra_rb_lo_ve_no_fl_al at 0x7fec5c8550c8>]}, '101000001011': {'0': ['SF', <function enc_ra_no_fl at 0x7fec5c855578>]}}

bits_to_op = defaultdict(dict)
for op, bits in op_bits.items():
    b1, b2 = bits[0], 0
    if len(bits) >= 2:
        b2 = bits[1]
    bits_to_op[b1][b2] = op
