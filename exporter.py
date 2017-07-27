def ra_rb_of_re(opcode,ra,rb,regcount,adjust,mem):
    ret = 0
    ret = ret | (opcode << 47)
    ret = ret | (ra << 42)
    ret = ret | (rb << 37)
    ret = ret | (regcount << 32)
    ret = ret | (adjust << 30)
    ret = ret | (mem << 3)
    return (ret,6)

def ra_rb_rc(opcode,ra,rb,rc,signed_unsigned,uf):
    ret = 0
    ret = ret | (opcode << 20)
    ret = ret | (ra << 15)
    ret = ret | (rb << 10)
    ret = ret | (rc << 5)
    ret = ret | (signed_unsigned << 2)
    ret = ret | (uf << 0)
    return (ret,3)

def ra_rb_im(opcode,ra,rb,imm,signed_unsigned,q,uf):
    ret = 0
    ret = ret | (opcode << 20)
    ret = ret | (ra << 15)
    ret = ret | (rb << 10)
    ret = ret | (imm << 5)
    ret = ret | (signed_unsigned << 2)
    ret = ret | (q << 1)
    ret = ret | (uf << 0)
    return (ret,3)

def ra_rb_lo_op(opcode,ra,rb,instruction_specific,uf):
    ret = 0
    ret = ret | (opcode << 18)
    ret = ret | (ra << 13)
    ret = ret | (rb << 8)
    ret = ret | (instruction_specific << 1)
    ret = ret | (uf << 0)
    return (ret,3)

def ra_rb_me(opcode,ra,rb,memoryflags):
    ret = 0
    ret = ret | (opcode << 21)
    ret = ret | (ra << 16)
    ret = ret | (rb << 11)
    ret = ret | (1 << 10)
    ret = ret | (memoryflags << 8)
    return (ret,4)

def ra_rb_lo_ve_no_fl(opcode,ra,rb):
    ret = 0
    ret = ret | (opcode << 18)
    ret = ret | (ra << 13)
    ret = ret | (rb << 8)
    return (ret,3)

def ra_rb_lo_ve_no_fl_al(opcode,ra,rb):
    ret = 0
    ret = ret | (opcode << 20)
    ret = ret | (ra << 15)
    ret = ret | (rb << 10)
    return (ret,3)

def ra_rb_lo_ve_no_fl_al(opcode,ra,rb):
    ret = 0
    ret = ret | (opcode << 15)
    ret = ret | (ra << 10)
    ret = ret | (rb << 5)
    return (ret,3)

def ra_rb_sh_ve(opcode,ra,rb):
    ret = 0
    ret = ret | (opcode << 10)
    ret = ret | (ra << 5)
    ret = ret | (rb << 0)
    return (ret,2)

def ra_im(opcode,ra,imm):
    ret = 0
    ret = ret | (opcode << 19)
    ret = ret | (ra << 14)
    ret = ret | (imm << 0)
    return (ret,3)

def ra_im_al(opcode,ra,imm):
    ret = 0
    ret = ret | (opcode << 22)
    ret = ret | (ra << 17)
    ret = ret | (imm << 0)
    return (ret,3)

def co_ra(opcode,condition,ra):
    ret = 0
    ret = ret | (opcode << 12)
    ret = ret | (condition << 8)
    ret = ret | (ra << 3)
    return (ret,2)

def ra_no_fl(opcode,ra):
    ret = 0
    ret = ret | (opcode << 6)
    ret = ret | (ra << 1)
    return (ret,2)

def ra_wi_fl(opcode,ra,q,uf):
    ret = 0
    ret = ret | (opcode << 18)
    ret = ret | (ra << 13)
    ret = ret | (q << 1)
    ret = ret | (uf << 0)
    return (ret,3)

def co(opcode,condition,offset):
    ret = 0
    ret = ret | (opcode << 21)
    ret = ret | (condition << 17)
    ret = ret | (offset << 0)
    return (ret,3)

def lo(opcode,location):
    ret = 0
    ret = ret | (opcode << 27)
    ret = ret | (location << 0)
    return (ret,4)

def of(opcode,offset):
    ret = 0
    ret = ret | (opcode << 27)
    ret = ret | (offset << 0)
    return (ret,4)

def no_re(opcode):
    ret = 0
    ret = ret | (opcode << 0)
    return (ret,2)

