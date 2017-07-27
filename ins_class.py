import itertools

reg_list = ["r%02i"%(i) for i in range(28)] + ["st","ra","pc","fl"]

cond2mnem = {
    0b0000: 'n',
    0b0001: 'e',
    0b0010: 'l',
    0b0011: 'le',
    0b0100: 'g',
    0b0101: 'ge',
    0b0110: 'no',
    0b0111: 'o',

    0b1000: 'ns',
    0b1001: 's',
    0b1010: 'sl',
    0b1011: 'sle',
    0b1100: 'sg',
    0b1101: 'sge',
    0b1110: 'UNDEFINED', # TODO: quintuple-check that these are numbered consistently between here/page19 of the manual/the emulator
    0b1111: '',
    }

mnem2cond = {k: v for (v,k) in cond2mnem.items()}

branch_ops = {base+k: (base, v) for (base, (k, v)) in itertools.product(['b', 'c', 'br', 'cr'], mnem2cond.items())}

class Reg:
    def __init__(self,name):
        self.name = name.lower()
        if self.name.startswith('r') and self.name != 'ra':
            self.num = int(self.name[1:], 10)
        else:
            self.num = reg_list.index(self.name)
        if self.num < 0 or self.num > 31:
            raise Exception("Invalid register number %d (name: %r)" % (self.num, name))
    def __repr__(self):
        return 'Reg(%r, %r)' % (self.name, self.num)
    def __str__(self):
        return reg_list[self.num]
    def untyped_repr(self, _):
        return [self.num]

class Imm:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return 'Imm(%r)' % value
    def __str__(self):
        return str(value)
    def untyped_repr(self, _):
        return [self.value]

class Mem:
    def __init__(self, reg, offset, regcount):
        self.reg = Reg(reg)
        self.offset = offset
        self.regcount = regcount
    def __repr__(self):
        return 'Mem(%r, %r, %r)' % (self.reg, self.offset, self.regcount)
    def __str__(self):
        return '[%s + %#x, %d]' % (self.reg, self.offset, self.regcount)
    def untyped_repr(self, labels):
        return [self.reg.untyped_repr(labels), self.offset, self.regcount]

class Ins:
    def __init__(self, name, uf, ops):
        self.name = name.lower()
        self.uf = uf
        self.ops = ops
        if self.name in branch_ops:
            self.name, cond = branch_ops[self.name]
            self.ops = [Condition(cond)] + self.ops
    def __repr__(self):
        return 'Ins(%r, %r, %r)' % (self.name, self.uf, self.ops)
    def __str__(self):
        return '%s%s %s' % (self.name, ('.' if self.uf else ''), ', '.join(map(str, self.ops)))

class Label:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Label(%r)' % self.name
    def __str__(self):
        return '&%s' % (self.name,)
    def untyped_repr(self, labels):
        if not labels:
            return [0]
        raise Exception("Unimplemented")

class MemoryFlags:
    def __init__(self, value):
        if value < 0 or value > 3:
            raise Exception("Invalid memory protection %d" % (num,))
        self.value = value
    def __repr__(self):
        return 'MemoryFlags(%d)' % self.value
    def __str__(self):
        return {0: 'MemoryFlags(---)',
                1: 'MemoryFlags(r--)',
                2: 'MemoryFlags(rw-)',
                3: 'MemoryFlags(r-x)',
                }[self.value]
    def untyped_repr(self, _):
        return [self.value]

class Condition:
    def __init__(self, value):
        if value < 0 or value > 15:
            raise Exception("Invalid memory protection %d" % (num,))
        self.value = value
    def __repr__(self):
        return 'Condition(%d)' % self.value
    def __str__(self):
        return 'Condition(%s)' % cond2mnem[self.value]
    def untyped_repr(self, _):
        return [self.value]
