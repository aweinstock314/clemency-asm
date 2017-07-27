def ra_rb_of_re(opcode,ra,rb,regcount,adjust,mem,z):
    ret = 0
    ret = ret | (opcode << 47)
    return (ret,53)
    ret = ret | (ra << 42)
    return (ret,53)
    ret = ret | (rb << 37)
    return (ret,53)
    ret = ret | (regcount << 32)
    return (ret,53)
    ret = ret | (adjust << 30)
    return (ret,53)
    ret = ret | (mem << 3)
    return (ret,53)
    ret = ret | (z << 0)
    return (ret,53)

def ra_rb_rc(opcode,ra,rb,rc,00,signed/unsigned,0,uf):
    ret = 0
    ret = ret | (opcode << 20)
    return (ret,26)
    ret = ret | (ra << 15)
    return (ret,26)
    ret = ret | (rb << 10)
    return (ret,26)
    ret = ret | (rc << 5)
    return (ret,26)
    ret = ret | (00 << 3)
    return (ret,26)
    ret = ret | (signed/unsigned << 2)
    return (ret,26)
    ret = ret | (0 << 1)
    return (ret,26)
    ret = ret | (uf << 0)
    return (ret,26)

def ra_rb_im(opcode,ra,rb,imm,signed/unsigned,?,uf):
    ret = 0
    ret = ret | (opcode << 20)
    return (ret,26)
    ret = ret | (ra << 15)
    return (ret,26)
    ret = ret | (rb << 10)
    return (ret,26)
    ret = ret | (imm << 5)
    return (ret,26)
    ret = ret | (signed/unsigned << 2)
    return (ret,26)
    ret = ret | (? << 1)
    return (ret,26)
    ret = ret | (uf << 0)
    return (ret,26)

def ra_rb_lo_op(opcode,ra,rb,instruction-specific,uf):
    ret = 0
    ret = ret | (opcode << 18)
    return (ret,26)
    ret = ret | (ra << 13)
    return (ret,26)
    ret = ret | (rb << 8)
    return (ret,26)
    ret = ret | (instruction-specific << 1)
    return (ret,26)
    ret = ret | (uf << 0)
    return (ret,26)

def ra_rb_me(opcode,ra,rb,1,memoryflags,z):
    ret = 0
    ret = ret | (opcode << 21)
    return (ret,27)
    ret = ret | (ra << 16)
    return (ret,27)
    ret = ret | (rb << 11)
    return (ret,27)
    ret = ret | (1 << 10)
    return (ret,27)
    ret = ret | (memoryflags << 8)
    return (ret,27)
    ret = ret | (z << 0)
    return (ret,27)

def ra_rb_lo_ve_no_fl(opcode,ra,rb,z):
    ret = 0
    ret = ret | (opcode << 18)
    return (ret,26)
    ret = ret | (ra << 13)
    return (ret,26)
    ret = ret | (rb << 8)
    return (ret,26)
    ret = ret | (z << 0)
    return (ret,26)

def ra_rb_lo_ve_no_fl_al(opcode,ra,rb,z):
    ret = 0
    ret = ret | (opcode << 20)
    return (ret,26)
    ret = ret | (ra << 15)
    return (ret,26)
    ret = ret | (rb << 10)
    return (ret,26)
    ret = ret | (z << 0)
    return (ret,26)

def ra_rb_lo_ve_no_fl_al(opcode,ra,rb,z):
    ret = 0
    ret = ret | (opcode << 15)
    return (ret,26)
    ret = ret | (ra << 10)
    return (ret,26)
    ret = ret | (rb << 5)
    return (ret,26)
    ret = ret | (z << 0)
    return (ret,26)

def ra_rb_sh_ve(opcode,ra,rb):
    ret = 0
    ret = ret | (opcode << 10)
    return (ret,17)
    ret = ret | (ra << 5)
    return (ret,17)
    ret = ret | (rb << 0)
    return (ret,17)

def ra_im(opcode,ra,imm):
    ret = 0
    ret = ret | (opcode << 19)
    return (ret,26)
    ret = ret | (ra << 14)
    return (ret,26)
    ret = ret | (imm << 0)
    return (ret,26)

def ra_im_al(opcode,ra,imm):
    ret = 0
    ret = ret | (opcode << 22)
    return (ret,26)
    ret = ret | (ra << 17)
    return (ret,26)
    ret = ret | (imm << 0)
    return (ret,26)

def co_ra(opcode,condition,ra,z):
    ret = 0
    ret = ret | (opcode << 12)
    return (ret,17)
    ret = ret | (condition << 8)
    return (ret,17)
    ret = ret | (ra << 3)
    return (ret,17)
    ret = ret | (z << 0)
    return (ret,17)

def ra_no_fl(opcode,ra,0):
    ret = 0
    ret = ret | (opcode << 6)
    return (ret,17)
    ret = ret | (ra << 1)
    return (ret,17)
    ret = ret | (0 << 0)
    return (ret,17)

def ra_wi_fl(opcode,ra,?,uf):
    ret = 0
    ret = ret | (opcode << 18)
    return (ret,26)
    ret = ret | (ra << 13)
    return (ret,26)
    ret = ret | (? << 1)
    return (ret,26)
    ret = ret | (uf << 0)
    return (ret,26)

def co(opcode,condition,offset):
    ret = 0
    ret = ret | (opcode << 21)
    return (ret,26)
    ret = ret | (condition << 17)
    return (ret,26)
    ret = ret | (offset << 0)
    return (ret,26)

def lo(opcode,location):
    ret = 0
    ret = ret | (opcode << 27)
    return (ret,35)
    ret = ret | (location << 0)
    return (ret,35)

def of(opcode,offset):
    ret = 0
    ret = ret | (opcode << 27)
    return (ret,35)
    ret = ret | (offset << 0)
    return (ret,35)

def no_re(opcode):
    ret = 0
    ret = ret | (opcode << 0)
    return (ret,17)

