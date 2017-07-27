import pdb

def ra_rb_of_re(opcode,opcode2,ra,rb,regcount,adjust,mem):

    ret = 0
    if len(bin(opcode)[2:]) > 7:
        return None
    ret = ret | (opcode << 47)
    if len(bin(ra)[2:]) > 5:
        return None
    ret = ret | (ra << 42)
    if len(bin(rb)[2:]) > 5:
        return None
    ret = ret | (rb << 37)
    if len(bin(regcount)[2:]) > 5:
        return None
    ret = ret | (regcount << 32)
    if len(bin(adjust)[2:]) > 2:
        return None
    ret = ret | (adjust << 30)
    if len(bin(mem)[2:]) > 27:
        return None
    ret = ret | (mem << 3)
    if len(bin(opcode2)[2:]) > 3:
        return None
    ret = ret | (opcode2 << 0)
    return (ret,6)

def ra_rb_rc(opcode,opcode2,ra,rb,rc,uf):

    ret = 0
    if len(bin(opcode)[2:]) > 7:
        return None
    ret = ret | (opcode << 20)
    if len(bin(ra)[2:]) > 5:
        return None
    ret = ret | (ra << 15)
    if len(bin(rb)[2:]) > 5:
        return None
    ret = ret | (rb << 10)
    if len(bin(rc)[2:]) > 5:
        return None
    ret = ret | (rc << 5)
    if len(bin(opcode2)[2:]) > 4:
        return None
    ret = ret | (opcode2 << 1)
    if len(bin(uf)[2:]) > 1:
        return None
    ret = ret | (uf << 0)
    return (ret,3)

def ra_rb_im(opcode,opcode2,ra,rb,imm,uf):

    ret = 0
    if len(bin(opcode)[2:]) > 7:
        return None
    ret = ret | (opcode << 20)
    if len(bin(ra)[2:]) > 5:
        return None
    ret = ret | (ra << 15)
    if len(bin(rb)[2:]) > 5:
        return None
    ret = ret | (rb << 10)
    if len(bin(imm)[2:]) > 5:
        return None
    ret = ret | (imm << 5)
    if len(bin(opcode2)[2:]) > 2:
        return None
    ret = ret | (opcode2 << 1)
    if len(bin(uf)[2:]) > 1:
        return None
    ret = ret | (uf << 0)
    return (ret,3)

def ra_rb_lo_op(opcode,ra,rb,instruction_specific,uf):

    ret = 0
    if len(bin(opcode)[2:]) > 9:
        return None
    ret = ret | (opcode << 18)
    if len(bin(ra)[2:]) > 5:
        return None
    ret = ret | (ra << 13)
    if len(bin(rb)[2:]) > 5:
        return None
    ret = ret | (rb << 8)
    if len(bin(instruction_specific)[2:]) > 7:
        return None
    ret = ret | (instruction_specific << 1)
    if len(bin(uf)[2:]) > 1:
        return None
    ret = ret | (uf << 0)
    return (ret,3)

def ra_rb_me(opcode,opcode2,ra,rb,one,memoryflags):

    ret = 0
    if len(bin(opcode)[2:]) > 7:
        return None
    ret = ret | (opcode << 21)
    if len(bin(ra)[2:]) > 5:
        return None
    ret = ret | (ra << 16)
    if len(bin(rb)[2:]) > 5:
        return None
    ret = ret | (rb << 11)
    if len(bin(one)[2:]) > 1:
        return None
    ret = ret | (one << 10)
    if len(bin(memoryflags)[2:]) > 2:
        return None
    ret = ret | (memoryflags << 8)
    if len(bin(opcode2)[2:]) > 8:
        return None
    ret = ret | (opcode2 << 0)
    return (ret,4)

def ra_rb_lo_ve_no_fl(opcode,opcode2,ra,rb):

    ret = 0
    if len(bin(opcode)[2:]) > 9:
        return None
    ret = ret | (opcode << 18)
    if len(bin(ra)[2:]) > 5:
        return None
    ret = ret | (ra << 13)
    if len(bin(rb)[2:]) > 5:
        return None
    ret = ret | (rb << 8)
    if len(bin(opcode2)[2:]) > 8:
        return None
    ret = ret | (opcode2 << 0)
    return (ret,3)

def ra_rb_lo_ve_no_fl_al(opcode,opcode2,ra,rb):

    ret = 0
    if len(bin(opcode)[2:]) > 7:
        return None
    ret = ret | (opcode << 20)
    if len(bin(ra)[2:]) > 5:
        return None
    ret = ret | (ra << 15)
    if len(bin(rb)[2:]) > 5:
        return None
    ret = ret | (rb << 10)
    if len(bin(opcode2)[2:]) > 10:
        return None
    ret = ret | (opcode2 << 0)
    return (ret,3)

def ra_rb_lo_ve_no_fl_al(opcode,opcode2,ra,rb):

    ret = 0
    if len(bin(opcode)[2:]) > 12:
        return None
    ret = ret | (opcode << 15)
    if len(bin(ra)[2:]) > 5:
        return None
    ret = ret | (ra << 10)
    if len(bin(rb)[2:]) > 5:
        return None
    ret = ret | (rb << 5)
    if len(bin(opcode2)[2:]) > 5:
        return None
    ret = ret | (opcode2 << 0)
    return (ret,3)

def ra_rb_sh_ve(opcode,ra,rb):

    ret = 0
    if len(bin(opcode)[2:]) > 8:
        return None
    ret = ret | (opcode << 10)
    if len(bin(ra)[2:]) > 5:
        return None
    ret = ret | (ra << 5)
    if len(bin(rb)[2:]) > 5:
        return None
    ret = ret | (rb << 0)
    return (ret,2)

def ra_im(opcode,ra,imm):

    ret = 0
    if len(bin(opcode)[2:]) > 8:
        return None
    ret = ret | (opcode << 19)
    if len(bin(ra)[2:]) > 5:
        return None
    ret = ret | (ra << 14)
    if len(bin(imm)[2:]) > 14:
        return None
    ret = ret | (imm << 0)
    return (ret,3)

def ra_im_al(opcode,ra,imm):

    ret = 0
    if len(bin(opcode)[2:]) > 5:
        return None
    ret = ret | (opcode << 22)
    if len(bin(ra)[2:]) > 5:
        return None
    ret = ret | (ra << 17)
    if len(bin(imm)[2:]) > 17:
        return None
    ret = ret | (imm << 0)
    return (ret,3)

def co_ra(opcode,opcode2,condition,ra):

    ret = 0
    if len(bin(opcode)[2:]) > 6:
        return None
    ret = ret | (opcode << 12)
    if len(bin(condition)[2:]) > 4:
        return None
    ret = ret | (condition << 8)
    if len(bin(ra)[2:]) > 5:
        return None
    ret = ret | (ra << 3)
    if len(bin(opcode2)[2:]) > 4:
        return None
    ret = ret | (opcode2 << 0)
    return (ret,2)

def ra_no_fl(opcode,opcode2,ra):

    ret = 0
    if len(bin(opcode)[2:]) > 12:
        return None
    ret = ret | (opcode << 6)
    if len(bin(ra)[2:]) > 5:
        return None
    ret = ret | (ra << 1)
    if len(bin(opcode2)[2:]) > 1:
        return None
    ret = ret | (opcode2 << 0)
    return (ret,2)

def ra_wi_fl(opcode,ra,q,uf):

    ret = 0
    if len(bin(opcode)[2:]) > 9:
        return None
    ret = ret | (opcode << 18)
    if len(bin(ra)[2:]) > 5:
        return None
    ret = ret | (ra << 13)
    if len(bin(q)[2:]) > 12:
        return None
    ret = ret | (q << 1)
    if len(bin(uf)[2:]) > 1:
        return None
    ret = ret | (uf << 0)
    return (ret,3)

def co(opcode,condition,offset):

    ret = 0
    if len(bin(opcode)[2:]) > 6:
        return None
    ret = ret | (opcode << 21)
    if len(bin(condition)[2:]) > 4:
        return None
    ret = ret | (condition << 17)
    if len(bin(offset)[2:]) > 17:
        return None
    ret = ret | (offset << 0)
    return (ret,3)

def lo(opcode,location):

    ret = 0
    if len(bin(opcode)[2:]) > 9:
        return None
    ret = ret | (opcode << 27)
    if len(bin(location)[2:]) > 27:
        return None
    ret = ret | (location << 0)
    return (ret,4)

def of(opcode,offset):

    ret = 0
    if len(bin(opcode)[2:]) > 9:
        return None
    ret = ret | (opcode << 27)
    if len(bin(offset)[2:]) > 27:
        return None
    ret = ret | (offset << 0)
    return (ret,4)

def no_re(opcode):

    ret = 0
    if len(bin(opcode)[2:]) > 18:
        return None
    ret = ret | (opcode << 0)
    return (ret,2)



fun_to_op = {'ra_rb_me': ['SMP'], 'ra_rb_rc': ['AD', 'ADC', 'ADCM', 'ADF', 'ADFM', 'ADM', 'AN', 'ANM', 'DMT', 'DV', 'DVF', 'DVFM', 'DVM', 'DVS', 'DVSM', 'MD', 'MDF', 'MDFM', 'MDM', 'MDS', 'MDSM', 'MU', 'MUF', 'MUFM', 'MUM', 'MUS', 'MUSM', 'OR', 'ORM', 'RL', 'RLM', 'RR', 'RRM', 'SA', 'SAM', 'SB', 'SBC', 'SBCM', 'SBF', 'SBFM', 'SBM', 'SL', 'SLM', 'SR', 'SRM', 'XR', 'XRM'], 'no_re': ['DBRK', 'HT', 'IR', 'RE', 'WT'], 'co_ra': ['BR', 'CR'], 'ra_rb_lo_ve_no_fl': ['FTI', 'FTIM', 'ITF', 'ITFM'], 'ra_rb_of_re': ['LDS', 'LDT', 'LDW', 'STS', 'STT', 'STW'], 'of': ['CAR'], 'ra_rb_lo_ve_no_fl_al': ['RMP', 'SES', 'SEW', 'ZES', 'ZEW'], 'ra_im_al': ['MH', 'ML', 'MS'], 'ra_rb_sh_ve': ['CM', 'CMF', 'CMFM', 'CMM'], 'ra_no_fl': ['DI', 'EI', 'RF', 'SF'], 'lo': ['BRA', 'BRR', 'CAA'], 'co': ['B', 'C'], 'ra_rb_lo_op': ['BF', 'BFM', 'NG', 'NGF', 'NGFM', 'NGM', 'NT', 'NTM'], 'ra_wi_fl': ['RND', 'RNDM'], 'ra_im': ['CMI', 'CMIM'], 'ra_rb_im': ['ADCI', 'ADCIM', 'ADI', 'ADIM', 'ANI', 'DVI', 'DVIM', 'DVIS', 'DVISM', 'MDI', 'MDIM', 'MDIS', 'MDISM', 'MUI', 'MUIM', 'MUIS', 'MUISM', 'ORI', 'RLI', 'RLIM', 'RRI', 'RRIM', 'SAI', 'SAIM', 'SBCI', 'SBCIM', 'SBI. SBIM', 'SLI', 'SLIM', 'SRI', 'SRIM', 'XRI']}

op_to_fun = {'BF': 'ra_rb_lo_op', 'MUSM': 'ra_rb_rc', 'CMF': 'ra_rb_sh_ve', 'MDISM': 'ra_rb_im', 'WT': 'no_re', 'BR': 'co_ra', 'DVI': 'ra_rb_im', 'RMP': 'ra_rb_lo_ve_no_fl_al', 'SAI': 'ra_rb_im', 'RR': 'ra_rb_rc', 'RE': 'no_re', 'RF': 'ra_no_fl', 'RL': 'ra_rb_rc', 'BFM': 'ra_rb_lo_op', 'CMFM': 'ra_rb_sh_ve', 'MDSM': 'ra_rb_rc', 'ADCIM': 'ra_rb_im', 'SBFM': 'ra_rb_rc', 'OR': 'ra_rb_rc', 'DVIS': 'ra_rb_im', 'CMM': 'ra_rb_sh_ve', 'NGM': 'ra_rb_lo_op', 'HT': 'no_re', 'FTIM': 'ra_rb_lo_ve_no_fl', 'DMT': 'ra_rb_rc', 'EI': 'ra_no_fl', 'SBCI': 'ra_rb_im', 'DVIM': 'ra_rb_im', 'SBCM': 'ra_rb_rc', 'ZES': 'ra_rb_lo_ve_no_fl_al', 'LDS': 'ra_rb_of_re', 'LDW': 'ra_rb_of_re', 'LDT': 'ra_rb_of_re', 'NTM': 'ra_rb_lo_op', 'XRM': 'ra_rb_rc', 'C': 'co', 'IR': 'no_re', 'XRI': 'ra_rb_im', 'CMIM': 'ra_im', 'ORI': 'ra_rb_im', 'MUISM': 'ra_rb_im', 'SBI. SBIM': 'ra_rb_im', 'MUFM': 'ra_rb_rc', 'FTI': 'ra_rb_lo_ve_no_fl', 'AN': 'ra_rb_rc', 'DVSM': 'ra_rb_rc', 'MD': 'ra_rb_rc', 'SAM': 'ra_rb_rc', 'RRIM': 'ra_rb_im', 'ANM': 'ra_rb_rc', 'SAIM': 'ra_rb_im', 'DBRK': 'no_re', 'ANI': 'ra_rb_im', 'RND': 'ra_wi_fl', 'MU': 'ra_rb_rc', 'MS': 'ra_im_al', 'SBCIM': 'ra_rb_im', 'DVM': 'ra_rb_rc', 'MDFM': 'ra_rb_rc', 'MUS': 'ra_rb_rc', 'DVF': 'ra_rb_rc', 'NGF': 'ra_rb_lo_op', 'SMP': 'ra_rb_me', 'MUF': 'ra_rb_rc', 'MUM': 'ra_rb_rc', 'MUI': 'ra_rb_im', 'DVS': 'ra_rb_rc', 'SEW': 'ra_rb_lo_ve_no_fl_al', 'RRM': 'ra_rb_rc', 'MDI': 'ra_rb_im', 'SES': 'ra_rb_lo_ve_no_fl_al', 'CMI': 'ra_im', 'RRI': 'ra_rb_im', 'MDM': 'ra_rb_rc', 'MDIM': 'ra_rb_im', 'MDF': 'ra_rb_rc', 'NG': 'ra_rb_lo_op', 'MDIS': 'ra_rb_im', 'MDS': 'ra_rb_rc', 'NT': 'ra_rb_lo_op', 'B': 'co', 'CM': 'ra_rb_sh_ve', 'ITFM': 'ra_rb_lo_ve_no_fl', 'MUIS': 'ra_rb_im', 'SLIM': 'ra_rb_im', 'SRM': 'ra_rb_rc', 'ADF': 'ra_rb_rc', 'DVFM': 'ra_rb_rc', 'MUIM': 'ra_rb_im', 'ADC': 'ra_rb_rc', 'XR': 'ra_rb_rc', 'CR': 'co_ra', 'DVISM': 'ra_rb_im', 'ADM': 'ra_rb_rc', 'ADIM': 'ra_rb_im', 'ADI': 'ra_rb_im', 'RLM': 'ra_rb_rc', 'RLI': 'ra_rb_im', 'ITF': 'ra_rb_lo_ve_no_fl', 'SR': 'ra_rb_rc', 'BRR': 'lo', 'SBC': 'ra_rb_rc', 'ORM': 'ra_rb_rc', 'SBF': 'ra_rb_rc', 'ZEW': 'ra_rb_lo_ve_no_fl_al', 'SL': 'ra_rb_rc', 'SB': 'ra_rb_rc', 'SA': 'ra_rb_rc', 'SF': 'ra_no_fl', 'BRA': 'lo', 'SBM': 'ra_rb_rc', 'DI': 'ra_no_fl', 'CAR': 'of', 'NGFM': 'ra_rb_lo_op', 'RNDM': 'ra_wi_fl', 'MH': 'ra_im_al', 'SRIM': 'ra_rb_im', 'DV': 'ra_rb_rc', 'CAA': 'lo', 'ML': 'ra_im_al', 'ADFM': 'ra_rb_rc', 'RLIM': 'ra_rb_im', 'SRI': 'ra_rb_im', 'AD': 'ra_rb_rc', 'ADCM': 'ra_rb_rc', 'ADCI': 'ra_rb_im', 'STT': 'ra_rb_of_re', 'SLM': 'ra_rb_rc', 'STW': 'ra_rb_of_re', 'SLI': 'ra_rb_im', 'STS': 'ra_rb_of_re'}

ops = {'AD':[0b000000,0b0000],
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
        'BR':[0b110010],
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
        'DI':[0b101000000101], 
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
        'EI':[0b101000000100], 
        'FTI':[0b101000101,0b00000000], 
        'FTIM':[0b101000111,0b00000000], 
        'HT':[0b101000000011000000], 
        'IR':[0b101000000001000000], 
        'ITF':[0b101000100,0b00000000], 
        'ITFM':[0b101000110,0b00000000], 
        'LDS':[0b1010100,0b000], 
        'LDT':[0b1010110,0b000], 
        'LDW':[0b1010101,0b000], 
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
        'NGFM':[0b101001111][0b0000000],
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
        'SEW':[0b1010000010000,0b00000], 
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
        'STT':[0b1011010,0b000], 
        'STW':[0b1011001,0b000], 
        'WT':[0b101000000010000000], 
        'XR':[0b0011100,0b0000], 
        'XRI':[0b0011100,0b01], 
        'XRM':[0b0011110,0b0000], 
        'ZES':[0b101000001001, 0b00000], 
        'ZEW':[0b101000001010,0b00000],}


def export(opcode,args):
    f = op_to_fun[opcode]
    return eval(f+"("+','.join([str(i) for i in ops["AD"]])+","+",".join(args) + ")")

print export("AD",["1","2","3","1"])

