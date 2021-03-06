from bits import *
from packers import *
import itertools

reg_list = ["r%02i"%(i) for i in range(29)] + ["st","ra","pc"] #,"fl"]
assert len(reg_list) == 32
#assert reg_list[31] == "fl"

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

raw_branch_ops = ['b', 'c', 'br', 'cr']
branch_ops = {base+k: (base, v) for (base, (k, v)) in itertools.product(raw_branch_ops, mnem2cond.items())}
inv_branch_ops = {k: v for (v,k) in branch_ops.items()}

class Reg:
    def __init__(self,name):
        if isinstance(name, type(0)):
            name = reg_list[name] # hack for number-passing
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
    def __init__(self, value, signedwidth=None):
        self.value = value
        self.signedwidth = signedwidth
    def __repr__(self):
        return 'Imm(%r)' % self.value
    def __str__(self):
        if self.signedwidth:
            return hex(signconversion(self.value, self.signedwidth))
        return hex(self.value)
    def untyped_repr(self, _):
        #return [self.value & ((1 << 9*3)-1)]
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
        #print 'mem', self.reg.untyped_repr(labels) + [self.offset, self.regcount]
        return self.reg.untyped_repr(labels) + [self.offset, self.regcount]

class Ins:
    def __init__(self, name, uf, ops):
        self.name = name.lower()
        self.uf = uf
        self.ops = ops
    def __repr__(self):
        return 'Ins(%r, %r, %r)' % (self.name, self.uf, self.ops)
    def __str__(self):
        return '%s%s %s' % (self.name, ('.' if self.uf else ''), ', '.join(map(str, self.ops)))
    def emit(self, data, i):
        processed_ops = []
        for op in self.ops:
            processed_ops.extend(op.untyped_repr((data, i)))
        processed_ops.append(self.uf)

        name = self.name.lower()
        if name in branch_ops:
            (name, cond) = branch_ops[name]
            processed_ops = [cond] + processed_ops

        from assembler import encode
        (value, size) = encode(name.upper(), processed_ops)
        return (value, size)
    def size(self):
        from maps import enc_op_to_fun
        name = self.name
        if name in branch_ops:
            name = branch_ops[name][0]
        name = name.upper()
        return enc_fun_to_size[enc_op_to_fun[name]]
    def location(self, selfaddr):
        if (self.name in branch_ops and branch_ops[self.name][0] in ['b', 'c']) or self.name in ['brr', 'car']:
            unsigned = self.ops[0].value
            width = 27 if self.name in ['brr', 'car'] else 17
            return selfaddr + signconversion(unsigned, width)
        if self.name in ['bra', 'caa']:
            return self.ops[0].value
        return None

class RawNytes:
    def __init__(self, nytes):
       self.nytes = nytes
    def emit(self, data, i):
        #print self.nytes
        return (nytes2num(self.nytes), len(self.nytes))

class Label:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Label(%r)' % self.name
    def __str__(self):
        return '&%s' % (self.name,)
    def untyped_repr(self, (data, i)):
        if not data:
            return [0]
        labels, sizes = data
        #print('labels: %r' % labels)
        #print('sizes: %r' % sizes)
        #print('i: %r' % i)
        cumulative_sizes = [0]
        total = 0
        for size in sizes:
            total += size
            cumulative_sizes.append(total)
        #print('cumulative_sizes: %r' % cumulative_sizes)
        #print cumulative_sizes[i]
        #print cumulative_sizes[labels[self.name]]
        relative = cumulative_sizes[labels[self.name]] - cumulative_sizes[i]
        #print('relative: %r' % relative)
        unsigned_relative = relative & ((1 << (27-10))-1)
        return [unsigned_relative]

class MemoryFlags:
    def __init__(self, value):
        if value < 0 or value > 3:
            raise Exception("Invalid memory protection %d" % (num,))
        self.value = value
    '''
    def __repr__(self):
        return 'MemoryFlags(%d)' % self.value
    '''
    def __repr__(self):
        return {0: 'MemoryFlags(---)',
                1: 'MemoryFlags(r--)',
                2: 'MemoryFlags(rw-)',
                3: 'MemoryFlags(r-x)',
                }[self.value]
    def __str__(self):
        from assembler import MP_MODES
        return MP_MODES[self.value]
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
