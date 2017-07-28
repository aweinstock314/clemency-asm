def ra_rb_of_re(opcode,opcode2,ra,rb,regcount,adjust,mem,uf):
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
    ret = ret | (imm << 3)
    if len(bin(opcode2)[2:]) > 2:
        return None
    ret = ret | (opcode2 << 1)
    if len(bin(uf)[2:]) > 1:
        return None
    ret = ret | (uf << 0)
    return (ret,3)

def ra_rb_lo_op(opcode,opcode2,ra,rb,uf):
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
    if len(bin(opcode2)[2:]) > 7:
        return None
    ret = ret | (opcode2 << 1)
    if len(bin(uf)[2:]) > 1:
        return None
    ret = ret | (uf << 0)
    return (ret,3)

def ra_rb_me(opcode,opcode2,ra,rb,memoryflags,uf):
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
    ret = ret | (1 << 9)
    if len(bin(memoryflags)[2:]) > 2:
        return None
    ret = ret | (memoryflags << 7)
    if len(bin(opcode2)[2:]) > 8:
        return None
    ret = ret | (opcode2 << 0)
    return (ret,4)

def ra_rb_lo_ve_no_fl(opcode,opcode2,ra,rb,uf):
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

def ra_rb_lo_ve_no_fl_al(opcode,opcode2,ra,rb,uf):
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

def ra_rb_lo_ve_no_fl_al(opcode,opcode2,ra,rb,uf):
    ret = 0
    if len(bin(opcode)[2:]) > 12:
        return None
    ret = ret | (opcode << 20)
    if len(bin(ra)[2:]) > 5:
        return None
    ret = ret | (ra << 15)
    if len(bin(rb)[2:]) > 5:
        return None
    ret = ret | (rb << 10)
    if len(bin(opcode2)[2:]) > 5:
        return None
    ret = ret | (opcode2 << 0)
    return (ret,3)

def ra_rb_sh_ve(opcode,ra,rb,uf):
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

def ra_im(opcode,ra,imm,uf):
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

def ra_im_al(opcode,ra,imm,uf):
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

def co_ra(opcode,opcode2,condition,ra,uf):
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

def ra_no_fl(opcode,opcode2,ra,uf):
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

def ra_wi_fl(opcode,opcode2,ra,uf):
    ret = 0
    if len(bin(opcode)[2:]) > 9:
        return None
    ret = ret | (opcode << 18)
    if len(bin(ra)[2:]) > 5:
        return None
    ret = ret | (ra << 13)
    if len(bin(opcode2)[2:]) > 12:
        return None
    ret = ret | (opcode2 << 1)
    if len(bin(uf)[2:]) > 1:
        return None
    ret = ret | (uf << 0)
    return (ret,3)

def co(opcode,condition,offset,uf):
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

def lo(opcode,location,uf):
    ret = 0
    if len(bin(opcode)[2:]) > 9:
        return None
    ret = ret | (opcode << 27)
    if len(bin(location)[2:]) > 27:
        return None
    ret = ret | (location << 0)
    return (ret,4)

def of(opcode,offset,uf):
    ret = 0
    if len(bin(opcode)[2:]) > 9:
        return None
    ret = ret | (opcode << 27)
    if len(bin(offset)[2:]) > 27:
        return None
    ret = ret | (offset << 0)
    return (ret,4)

def no_re(opcode,uf):
    ret = 0
    if len(bin(opcode)[2:]) > 18:
        return None
    ret = ret | (opcode << 0)
    return (ret,2)
