f = open("insts.txt").read()
f = f.split("\n\n")

import re
rex = re.compile("\[.*\]")

d1 = {}
d2 = {}
"""
for line in f:
    lines = line.split("\n")
    arg =  rex.search(lines[0]).group(0)
    name = lines[0].split(arg)[0]
    name = '_'.join([i[:2].lower() for i in name.split(" ")[:-1]])
  %  args = [i[:-1].split(' ') for i in arg.split('[')[1:]]
    arg_pos =  [int(i[0].split("-")[-1].lower()) for i in args]
    arg_start_pos =  [int(i[0].split("-")[0].lower()) for i in args]
    arg_name = [i[1].lower() for i in args]
    #print args
    #print arg_pos
    #print arg_name
    le = int(arg_pos[-1])
    sorted_names = list(arg_name)
    if 'opcode2' in sorted_names:
        sorted_names.remove('opcode2')
        sorted_names.insert(1, 'opcode2')
    if not 'uf' in sorted_names:
        sorted_names.append('uf')
    print "def enc_{}({}):".format(name.lower(),','.join(sorted_names))
    print "    ret = 0"
    for i,j in enumerate(arg_pos):
        print "    if {}.bit_length() > {}:".format(arg_name[i],j - arg_start_pos[i] + 1)
        print "        raise Exception('operand %s out of range {}' % {})".format(j - arg_start_pos[i] + 1, arg_name[i])
        print "    ret = ret | (" + str(arg_name[i]) + " << " + str(le - j) + ")"
    print "    return (ret,{})".format((le/9)+1)
    print
    print "def dec_{}(ins):".format(name.lower())
    print "    uf = False"
    for i, j in enumerate(arg_pos):
        print "    {} = (ins >> {}) & {}".format(arg_name[i], le - j, (1 << (j - arg_start_pos[i] + 1)) - 1)
    print "    return ({},), {}".format(','.join(sorted_names), (le/9)+1)
    print

    #print lines[1].split(",")
    
    if not name in d1:
        d1[name.strip()] = []
    for i in lines[1].split(","):
        d1[name.strip()].append(i.strip())
        d2[i.strip()] = name.strip()
"""

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

mask_d = {}


for line in f:
    lines = line.split("\n")
    op_names=  lines[1].split(',')
    arg =  rex.search(lines[0]).group(0)
    name = lines[0].split(arg)[0]
    name = '_'.join([i[:2].lower() for i in name.split(" ")[:-1]])
    args = [i[:-1].split(' ') for i in arg.split('[')[1:]]
    arg_pos =  [int(i[0].split("-")[-1].lower()) for i in args]
    arg_start_pos =  [int(i[0].split("-")[0].lower()) for i in args]
    arg_name = [i[1].lower() for i in args]
    #print args
    #print arg_pos
    #print arg_name
    mask = 0
    #print name
    #first loop
    for i,opcodez in enumerate(args):
        if opcodez[1].lower() in ["opcode","opcode2"]:
            for x in range(arg_start_pos[i], arg_pos[i]+1):
                mask = mask | (1 << x)

    #Reverse the bin
    mask = int(bin(mask)[2:][::-1],2)
    rev_mask = mask#~mask & ((1<<mask.bit_length())-1)
    #mask = bin(mask)[2:].replace("0","z").replace("1","0").replace("z","1")
    #print "MASK", bin(rev_mask)
    #second loop
    for nz in op_names:
        if nz.strip() not in ["LDTD","LDSD","LDWD"]:
            tmp_mask = 0
            nz = nz.strip()
            for i,opcodez in enumerate(args):
                if opcodez[1].lower() in ["opcode","opcode2"]:
                    #This is getting the length total at the end
                    le = max(map(int, arg_pos))
                    pos = le - arg_pos[i]
                    if opcodez[1].lower() == "opcode":
                        tmp_mask = tmp_mask |  (op_bits[nz][0] << pos)
                    else:
                        tmp_mask = tmp_mask |  (op_bits[nz][1] << pos)
            
            
            if not rev_mask in mask_d:
                mask_d[rev_mask] = []
            mask_d[rev_mask].append((tmp_mask,nz))

print mask_d
    
    
"""
print d1
print
print d2
"""
