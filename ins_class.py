
reg_list = ["r%02i"%(i) for i in range(29)] + ["st","ra","pc","fl"]

class Reg:
    def __init__(self,name):
        self.name = name.lower()
        if self.name.startswith('r'):
            self.num = int(self.name[1:], 10)
        else:
            self.num = reg_list.index(self.name)
        if self.num < 0 or self.num > 31:
            from assembler import ParseException
            raise ParseException(line, i, "Invalid register number %d" % (num,))
    def __repr__(self):
        return 'Reg(%r, %r)' % (self.name, self.num)
    def __str__(self):
        return self.name

class Imm:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return 'Imm(%r)' % value
    def __str__(self):
        return str(value)

class Mem:
    def __init__(self, reg, offset, regcount):
        self.reg = Reg(reg)
        self.offset = offset
        self.regcount = regcount
    def __repr__(self):
        return 'Mem(%r, %r, %r)' % (self.reg, self.offset, self.regcount)
    def __str__(self):
        return '[%s + %#x, %d]' % (self.reg, self.offset, self.regcount)

class Ins:
    def __init__(self, name, uf, ops):
        self.name = name
        self.uf = uf
        self.ops = ops
    def __repr__(self):
        return 'Ins(%r, %r, %r)' % (self.name, self.uf, self.ops)
    def __str__(self):
        return '%s%s %s' % (self.name, ('.' if self.uf else ''), ','.join(map(str, self.ops)))

class Label:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Label(%r)' % self.name
    def __str__(self):
        return '&%s' % (self.name,)
