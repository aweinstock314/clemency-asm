def enc_ra_rb_of_re(opcode,opcode2,ra,rb,mem,regcount,uf):
    ret = 0
    if opcode.bit_length() > 7:
        raise Exception('operand %s out of range 7' % opcode)
    ret = ret | (opcode << 47)
    if opcode2.bit_length() > 3:
        raise Exception('operand %s out of range 3' % opcode2)
    ret = ret | (opcode2 << 0)
    if ra.bit_length() > 5:
        raise Exception('operand %s out of range 5' % ra)
    ret = ret | (ra << 42)
    if rb.bit_length() > 5:
        raise Exception('operand %s out of range 5' % rb)
    ret = ret | (rb << 37)
    ret = ret | (0 << 30)
    if mem.bit_length() > 27:
        raise Exception('operand %s out of range 27' % mem)
    ret = ret | (mem << 3)
    if regcount.bit_length() > 5:
        raise Exception('operand %s out of range 5' % regcount)
    if regcount == 0:
        raise Exception('negative regcount')
    ret = ret | ((regcount-1) << 32)
    return (ret,6)

def dec_ra_rb_of_re(ins):
    uf = False
    opcode = (ins >> 47) & 127
    opcode2 = (ins >> 0) & 7
    ra = (ins >> 42) & 31
    rb = (ins >> 37) & 31
    assert ((ins >> 30) & 3) == 0
    mem = (ins >> 3) & 134217727
    regcount = (ins >> 32) & 31
    return (opcode,opcode2,ra,rb,mem,regcount,uf,), 6

def enc_ra_rb_of_re_i(opcode,opcode2,ra,rb,mem,regcount,uf):
    ret = 0
    if opcode.bit_length() > 7:
        raise Exception('operand %s out of range 7' % opcode)
    ret = ret | (opcode << 47)
    if opcode2.bit_length() > 3:
        raise Exception('operand %s out of range 3' % opcode2)
    ret = ret | (opcode2 << 0)
    if ra.bit_length() > 5:
        raise Exception('operand %s out of range 5' % ra)
    ret = ret | (ra << 42)
    if rb.bit_length() > 5:
        raise Exception('operand %s out of range 5' % rb)
    ret = ret | (rb << 37)
    ret = ret | (1 << 30)
    if mem.bit_length() > 27:
        raise Exception('operand %s out of range 27' % mem)
    ret = ret | (mem << 3)
    if regcount.bit_length() > 5:
        raise Exception('operand %s out of range 5' % regcount)
    if regcount == 0:
        raise Exception('negative regcount')
    ret = ret | ((regcount-1) << 32)
    return (ret,6)

def dec_ra_rb_of_re_i(ins):
    uf = False
    opcode = (ins >> 47) & 127
    opcode2 = (ins >> 0) & 7
    ra = (ins >> 42) & 31
    rb = (ins >> 37) & 31
    assert ((ins >> 30) & 3) == 1
    mem = (ins >> 3) & 134217727
    regcount = (ins >> 32) & 31
    return (opcode,opcode2,ra,rb,mem,regcount,uf,), 6

def enc_ra_rb_of_re_d(opcode,opcode2,ra,rb,mem,regcount,uf):
    ret = 0
    if opcode.bit_length() > 7:
        raise Exception('operand %s out of range 7' % opcode)
    ret = ret | (opcode << 47)
    if opcode2.bit_length() > 3:
        raise Exception('operand %s out of range 3' % opcode2)
    ret = ret | (opcode2 << 0)
    if ra.bit_length() > 5:
        raise Exception('operand %s out of range 5' % ra)
    ret = ret | (ra << 42)
    if rb.bit_length() > 5:
        raise Exception('operand %s out of range 5' % rb)
    ret = ret | (rb << 37)
    ret = ret | (2 << 30)
    if mem.bit_length() > 27:
        raise Exception('operand %s out of range 27' % mem)
    ret = ret | (mem << 3)
    if regcount.bit_length() > 5:
        raise Exception('operand %s out of range 5' % regcount)
    if regcount == 0:
        raise Exception('negative regcount')
    ret = ret | ((regcount-1) << 32)
    return (ret,6)

def dec_ra_rb_of_re_d(ins):
    uf = False
    opcode = (ins >> 47) & 127
    opcode2 = (ins >> 0) & 7
    ra = (ins >> 42) & 31
    rb = (ins >> 37) & 31
    assert ((ins >> 30) & 3) == 2
    mem = (ins >> 3) & 134217727
    regcount = (ins >> 32) & 31
    return (opcode,opcode2,ra,rb,mem,regcount,uf,), 6

def enc_ra_rb_rc(opcode,opcode2,ra,rb,rc,uf):
    ret = 0
    if opcode.bit_length() > 7:
        raise Exception('operand %s out of range 7' % opcode)
    ret = ret | (opcode << 20)
    if opcode2.bit_length() > 4:
        raise Exception('operand %s out of range 4' % opcode2)
    ret = ret | (opcode2 << 1)
    if ra.bit_length() > 5:
        raise Exception('operand %s out of range 5' % ra)
    ret = ret | (ra << 15)
    if rb.bit_length() > 5:
        raise Exception('operand %s out of range 5' % rb)
    ret = ret | (rb << 10)
    if rc.bit_length() > 5:
        raise Exception('operand %s out of range 5' % rc)
    ret = ret | (rc << 5)
    if uf.bit_length() > 1:
        raise Exception('operand %s out of range 1' % uf)
    ret = ret | (uf << 0)
    return (ret,3)

def dec_ra_rb_rc(ins):
    uf = False
    opcode = (ins >> 20) & 127
    opcode2 = (ins >> 1) & 15
    ra = (ins >> 15) & 31
    rb = (ins >> 10) & 31
    rc = (ins >> 5) & 31
    uf = (ins >> 0) & 1
    return (opcode,opcode2,ra,rb,rc,uf,), 3

def enc_ra_rb_im(opcode,opcode2,ra,rb,imm,uf):
    ret = 0
    if opcode.bit_length() > 7:
        raise Exception('operand %s out of range 7' % opcode)
    ret = ret | (opcode << 20)
    if opcode2.bit_length() > 2:
        raise Exception('operand %s out of range 2' % opcode2)
    ret = ret | (opcode2 << 1)
    if ra.bit_length() > 5:
        raise Exception('operand %s out of range 5' % ra)
    ret = ret | (ra << 15)
    if rb.bit_length() > 5:
        raise Exception('operand %s out of range 5' % rb)
    ret = ret | (rb << 10)
    if imm.bit_length() > 7:
        raise Exception('operand %s out of range 7' % imm)
    ret = ret | (imm << 3)
    if uf.bit_length() > 1:
        raise Exception('operand %s out of range 1' % uf)
    ret = ret | (uf << 0)
    return (ret,3)

def dec_ra_rb_im(ins):
    uf = False
    opcode = (ins >> 20) & 127
    opcode2 = (ins >> 1) & 3
    ra = (ins >> 15) & 31
    rb = (ins >> 10) & 31
    imm = (ins >> 3) & 127
    uf = (ins >> 0) & 1
    return (opcode,opcode2,ra,rb,imm,uf,), 3

def enc_ra_rb_lo_op(opcode,opcode2,ra,rb,uf):
    ret = 0
    if opcode.bit_length() > 9:
        raise Exception('operand %s out of range 9' % opcode)
    ret = ret | (opcode << 18)
    if opcode2.bit_length() > 7:
        raise Exception('operand %s out of range 7' % opcode2)
    ret = ret | (opcode2 << 1)
    if ra.bit_length() > 5:
        raise Exception('operand %s out of range 5' % ra)
    ret = ret | (ra << 13)
    if rb.bit_length() > 5:
        raise Exception('operand %s out of range 5' % rb)
    ret = ret | (rb << 8)
    if uf.bit_length() > 1:
        raise Exception('operand %s out of range 1' % uf)
    ret = ret | (uf << 0)
    return (ret,3)

def dec_ra_rb_lo_op(ins):
    uf = False
    opcode = (ins >> 18) & 511
    opcode2 = (ins >> 1) & 127
    ra = (ins >> 13) & 31
    rb = (ins >> 8) & 31
    uf = (ins >> 0) & 1
    return (opcode,opcode2,ra,rb,uf,), 3

def enc_ra_rb_me(opcode,opcode2,ra,rb,memoryflags,uf):
    ret = 0
    if opcode.bit_length() > 7:
        raise Exception('operand %s out of range 7' % opcode)
    ret = ret | (opcode << 20)
    if opcode2.bit_length() > 7:
        raise Exception('operand %s out of range 7' % opcode2)
    ret = ret | (opcode2 << 0)
    if ra.bit_length() > 5:
        raise Exception('operand %s out of range 5' % ra)
    ret = ret | (ra << 15)
    if rb.bit_length() > 5:
        raise Exception('operand %s out of range 5' % rb)
    ret = ret | (rb << 10)
    ret = ret | (1 << 9)
    if memoryflags.bit_length() > 2:
        raise Exception('operand %s out of range 2' % memoryflags)
    ret = ret | (memoryflags << 7)
    return (ret,3)

def dec_ra_rb_me(ins):
    uf = False
    opcode = (ins >> 20) & 127
    opcode2 = (ins >> 0) & 127
    ra = (ins >> 15) & 31
    rb = (ins >> 10) & 31
    assert ((ins >> 9) & 1) == 1
    memoryflags = (ins >> 7) & 3
    return (opcode,opcode2,ra,rb,memoryflags,uf,), 3

def enc_ra_rb_lo_ve_no_fl(opcode,opcode2,ra,rb,uf):
    ret = 0
    if opcode.bit_length() > 9:
        raise Exception('operand %s out of range 9' % opcode)
    ret = ret | (opcode << 18)
    if opcode2.bit_length() > 8:
        raise Exception('operand %s out of range 8' % opcode2)
    ret = ret | (opcode2 << 0)
    if ra.bit_length() > 5:
        raise Exception('operand %s out of range 5' % ra)
    ret = ret | (ra << 13)
    if rb.bit_length() > 5:
        raise Exception('operand %s out of range 5' % rb)
    ret = ret | (rb << 8)
    return (ret,3)

def dec_ra_rb_lo_ve_no_fl(ins):
    uf = False
    opcode = (ins >> 18) & 511
    opcode2 = (ins >> 0) & 255
    ra = (ins >> 13) & 31
    rb = (ins >> 8) & 31
    return (opcode,opcode2,ra,rb,uf,), 3

def enc_ra_rb_lo_ve_no_fl_al(opcode,opcode2,ra,rb,uf):
    ret = 0
    if opcode.bit_length() > 7:
        raise Exception('operand %s out of range 7' % opcode)
    ret = ret | (opcode << 20)
    if opcode2.bit_length() > 10:
        raise Exception('operand %s out of range 10' % opcode2)
    ret = ret | (opcode2 << 0)
    if ra.bit_length() > 5:
        raise Exception('operand %s out of range 5' % ra)
    ret = ret | (ra << 15)
    if rb.bit_length() > 5:
        raise Exception('operand %s out of range 5' % rb)
    ret = ret | (rb << 10)
    return (ret,3)

def dec_ra_rb_lo_ve_no_fl_al(ins):
    uf = False
    opcode = (ins >> 20) & 127
    opcode2 = (ins >> 0) & 1023
    ra = (ins >> 15) & 31
    rb = (ins >> 10) & 31
    return (opcode,opcode2,ra,rb,uf,), 3

def enc_ra_rb_lo_ve_no_fl_al_tw(opcode,opcode2,ra,rb,uf):
    ret = 0
    if opcode.bit_length() > 12:
        raise Exception('operand %s out of range 12' % opcode)
    ret = ret | (opcode << 15)
    if opcode2.bit_length() > 5:
        raise Exception('operand %s out of range 5' % opcode2)
    ret = ret | (opcode2 << 0)
    if ra.bit_length() > 5:
        raise Exception('operand %s out of range 5' % ra)
    ret = ret | (ra << 10)
    if rb.bit_length() > 5:
        raise Exception('operand %s out of range 5' % rb)
    ret = ret | (rb << 5)
    return (ret,3)

def dec_ra_rb_lo_ve_no_fl_al_tw(ins):
    uf = False
    opcode = (ins >> 15) & 4095
    opcode2 = (ins >> 0) & 31
    ra = (ins >> 10) & 31
    rb = (ins >> 5) & 31
    return (opcode,opcode2,ra,rb,uf,), 3

def enc_ra_rb_sh_ve(opcode,ra,rb,uf):
    ret = 0
    if opcode.bit_length() > 8:
        raise Exception('operand %s out of range 8' % opcode)
    ret = ret | (opcode << 10)
    if ra.bit_length() > 5:
        raise Exception('operand %s out of range 5' % ra)
    ret = ret | (ra << 5)
    if rb.bit_length() > 5:
        raise Exception('operand %s out of range 5' % rb)
    ret = ret | (rb << 0)
    return (ret,2)

def dec_ra_rb_sh_ve(ins):
    uf = False
    opcode = (ins >> 10) & 255
    ra = (ins >> 5) & 31
    rb = (ins >> 0) & 31
    return (opcode,ra,rb,uf,), 2

def enc_ra_im(opcode,ra,imm,uf):
    ret = 0
    if opcode.bit_length() > 8:
        raise Exception('operand %s out of range 8' % opcode)
    ret = ret | (opcode << 19)
    if ra.bit_length() > 5:
        raise Exception('operand %s out of range 5' % ra)
    ret = ret | (ra << 14)
    if imm.bit_length() > 14:
        raise Exception('operand %s out of range 14' % imm)
    ret = ret | (imm << 0)
    return (ret,3)

def dec_ra_im(ins):
    uf = False
    opcode = (ins >> 19) & 255
    ra = (ins >> 14) & 31
    imm = (ins >> 0) & 16383
    return (opcode,ra,imm,uf,), 3

def enc_ra_im_al(opcode,ra,imm,uf):
    ret = 0
    if opcode.bit_length() > 5:
        raise Exception('operand %s out of range 5' % opcode)
    ret = ret | (opcode << 22)
    if ra.bit_length() > 5:
        raise Exception('operand %s out of range 5' % ra)
    ret = ret | (ra << 17)
    if imm.bit_length() > 17:
        raise Exception('operand %s out of range 17' % imm)
    ret = ret | (imm << 0)
    return (ret,3)

def dec_ra_im_al(ins):
    uf = False
    opcode = (ins >> 22) & 31
    ra = (ins >> 17) & 31
    imm = (ins >> 0) & 131071
    return (opcode,ra,imm,uf,), 3

def enc_co_ra(opcode,opcode2,condition,ra,uf):
    ret = 0
    if opcode.bit_length() > 6:
        raise Exception('operand %s out of range 6' % opcode)
    ret = ret | (opcode << 12)
    if opcode2.bit_length() > 4:
        raise Exception('operand %s out of range 4' % opcode2)
    ret = ret | (opcode2 << 0)
    if condition.bit_length() > 4:
        raise Exception('operand %s out of range 4' % condition)
    ret = ret | (condition << 8)
    if ra.bit_length() > 5:
        raise Exception('operand %s out of range 5' % ra)
    ret = ret | (ra << 3)
    return (ret,2)

def dec_co_ra(ins):
    uf = False
    opcode = (ins >> 12) & 63
    opcode2 = (ins >> 0) & 15
    condition = (ins >> 8) & 15
    ra = (ins >> 3) & 31
    return (opcode,opcode2,condition,ra,uf,), 2

def enc_ra_no_fl(opcode,opcode2,ra,uf):
    ret = 0
    if opcode.bit_length() > 12:
        raise Exception('operand %s out of range 12' % opcode)
    ret = ret | (opcode << 6)
    if opcode2.bit_length() > 1:
        raise Exception('operand %s out of range 1' % opcode2)
    ret = ret | (opcode2 << 0)
    if ra.bit_length() > 5:
        raise Exception('operand %s out of range 5' % ra)
    ret = ret | (ra << 1)
    return (ret,2)

def dec_ra_no_fl(ins):
    uf = False
    opcode = (ins >> 6) & 4095
    opcode2 = (ins >> 0) & 1
    ra = (ins >> 1) & 31
    return (opcode,opcode2,ra,uf,), 2

def enc_ra_wi_fl(opcode,opcode2,ra,uf):
    ret = 0
    if opcode.bit_length() > 9:
        raise Exception('operand %s out of range 9' % opcode)
    ret = ret | (opcode << 18)
    if opcode2.bit_length() > 12:
        raise Exception('operand %s out of range 12' % opcode2)
    ret = ret | (opcode2 << 1)
    if ra.bit_length() > 5:
        raise Exception('operand %s out of range 5' % ra)
    ret = ret | (ra << 13)
    if uf.bit_length() > 1:
        raise Exception('operand %s out of range 1' % uf)
    ret = ret | (uf << 0)
    return (ret,3)

def dec_ra_wi_fl(ins):
    uf = False
    opcode = (ins >> 18) & 511
    opcode2 = (ins >> 1) & 4095
    ra = (ins >> 13) & 31
    uf = (ins >> 0) & 1
    return (opcode,opcode2,ra,uf,), 3

def enc_co(opcode,condition,offset,uf):
    ret = 0
    if opcode.bit_length() > 6:
        raise Exception('operand %s out of range 6' % opcode)
    ret = ret | (opcode << 21)
    if condition.bit_length() > 4:
        raise Exception('operand %s out of range 4' % condition)
    ret = ret | (condition << 17)
    if offset.bit_length() > 17:
        raise Exception('operand %s out of range 17' % offset)
    ret = ret | (offset << 0)
    return (ret,3)

def dec_co(ins):
    uf = False
    opcode = (ins >> 21) & 63
    condition = (ins >> 17) & 15
    offset = (ins >> 0) & 131071
    return (opcode,condition,offset,uf,), 3

def enc_lo(opcode,location,uf):
    ret = 0
    if opcode.bit_length() > 9:
        raise Exception('operand %s out of range 9' % opcode)
    ret = ret | (opcode << 27)
    if location.bit_length() > 27:
        raise Exception('operand %s out of range 27' % location)
    ret = ret | (location << 0)
    return (ret,4)

def dec_lo(ins):
    uf = False
    opcode = (ins >> 27) & 511
    location = (ins >> 0) & 134217727
    return (opcode,location,uf,), 4

def enc_of(opcode,offset,uf):
    ret = 0
    if opcode.bit_length() > 9:
        raise Exception('operand %s out of range 9' % opcode)
    ret = ret | (opcode << 27)
    if offset.bit_length() > 27:
        raise Exception('operand %s out of range 27' % offset)
    ret = ret | (offset << 0)
    return (ret,4)

def dec_of(ins):
    uf = False
    opcode = (ins >> 27) & 511
    offset = (ins >> 0) & 134217727
    return (opcode,offset,uf,), 4

def enc_no_re(opcode,uf):
    ret = 0
    if opcode.bit_length() > 18:
        raise Exception('operand %s out of range 18' % opcode)
    ret = ret | (opcode << 0)
    return (ret,2)

def dec_no_re(ins):
    uf = False
    opcode = (ins >> 0) & 262143
    return (opcode,uf,), 2

