#!/usr/bin/env python2
from ins_class import *

formats = [
    ((Reg, Mem), ['LDS', 'LDT', 'LDW', 'STS', 'STT', 'STW']),
    ((Reg, Reg, Reg), ['AD', 'ADC', 'ADCM', 'ADF', 'ADFM', 'ADM', 'AN', 'ANM', 'DMT', 'DV', 'DVF', 'DVFM', 'DVM', 'DVS', 'DVSM', 'MD', 'MDF', 'MDFM', 'MDM', 'MDS', 'MDSM', 'MU', 'MUF', 'MUFM', 'MUM', 'MUS', 'MUSM', 'OR', 'ORM', 'RL', 'RLM', 'RR', 'RRM', 'SA', 'SAM', 'SB', 'SBC', 'SBCM', 'SBF', 'SBFM', 'SBM', 'SL', 'SLM', 'SR', 'SRM', 'XR', 'XRM']),
    ((Reg, Reg, Imm), ['ADCI', 'ADCIM', 'ADI', 'ADIM', 'ANI', 'DVI', 'DVIM', 'DVIS', 'DVISM', 'MDI', 'MDIM', 'MDIS', 'MDISM', 'MUI', 'MUIM', 'MUIS', 'MUISM', 'ORI', 'RLI', 'RLIM', 'RRI', 'RRIM', 'SAI', 'SAIM', 'SBCI', 'SBCIM', 'SBI', 'SBIM', 'SLI', 'SLIM', 'SRI', 'SRIM', 'XRI']),

    # TODO: figure out if "Logical Operation" in the RTF is significant
    ((Reg, Reg), ['BF', 'BFM', 'NG', 'NGF', 'NGFM', 'NGM', 'NT', 'NTM']),

    ((Reg, Reg, MemoryFlags), ['SMP']),

    # TODO: "{long,short} version no flag {,alt,alt2}"
    ((Reg, Reg), ['FTI', 'FTIM', 'ITF', 'ITFM']),
    ((Reg, Reg), ['RMP']),
    ((Reg, Reg), ['SES', 'SEW', 'ZES', 'ZEW']),
    ((Reg, Reg), ['CM', 'CMF' ,'CMFM', 'CMM']),

    ((Reg, Imm), ['CMI', 'CMIM']),
    ((Reg, Imm), ['MH', 'ML', 'MS']),

    ((Condition, Reg), ['BR', 'CR']),

    ((Reg,), ['DI', 'EI', 'RF', 'SF']), # these instructions can't set the UF (and their representations don't have a bit for it)
    ((Reg,), ['RND', 'RNDM']), # these instructions can

    ((Condition, Imm), ['B', 'C']),

    # TODO: "Location" class, possibly?
    ((Imm,), ['BRA', 'BRR', 'CAA']),
    # TODO: "Offset" class?
    ((Imm,), ['CAR']),

    ((), ['DBRK', 'HT', 'IR', 'RE', 'WT']),
    ]

def generate():
    forward = {}
    backward = {}

    for (template, instrs) in formats:
        for instr in instrs:
            forward[instr] = template
            tmp = backward.get(template, list())
            backward[template] = tmp
            tmp.append(instr)

    return forward, backward

if __name__ == '__main__':
    forward, backward = generate()
    print(forward)
    print(backward)
