#!/usr/bin/env python2
from ins_class import *
import itertools

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

def all_possible_for_class(cls):
    if cls == Reg:
        #return [Reg(x) for x in reg_list]
        return [Reg(x) for x in 'r00', 'r01', 'r02', 'ra', 'pc']
    elif cls == Mem:
        ret = []
        for reg in all_possible_for_class(Reg):
            for off in all_possible_for_class(Imm):
                for regcount in all_possible_for_class(Imm):
                    ret.append(Mem(reg.name, off.value, regcount.value))
        return ret
    elif cls == Imm:
        return [Imm(1), Imm(2), Imm(5)] # TODO: more representative extrema?
    elif cls == MemoryFlags:
        return [MemoryFlags(i) for i in range(4)]
    elif cls == Condition:
        ret = list(range(16))
        ret.remove(0b1110)
        return [Condition(i) for i in ret]
    elif cls == Ins:
        forward, backward = generate()
        ret = []
        for instr, template in forward.items():
            instr = instr.lower()
            for ops in itertools.product(*[all_possible_for_class(x) for x in template]):
                uf = False # TODO: both?
                if instr in raw_branch_ops:
                    #print('; %r %r' % (instr, ops))
                    name = inv_branch_ops[instr, ops[0].value]
                    ops = ops[1:]
                else:
                    name = instr
                    #print('; %r %r' % (instr, ops))
                ret.append(Ins(name, uf, list(ops)))
        return ret

if __name__ == '__main__':
    forward, backward = generate()
    # use this with something like 'python2 corpus.py > tmp.clemency'
    for instr in all_possible_for_class(Ins):
        #print('#' + repr(instr))
        print(str(instr))
