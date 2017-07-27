

reg_list = ["r%i"%(i) for i in range(29)]
reg_list = reg_list + ["st","ra","pc","fl"]

class Reg:
    ""
    name = ""
    number = 0
    size = 27#in bits
    def __init__(self,name,sz):
        ""
        self.name = name.lower
        self.number = reg_list.index(self.name)

class Imm:
    ""
    value = 0
    def __init__(self,value):
        self.value = value

class Mem:
    ""
    base = 0
    offset = 0
    def __init__(self):
        ""

class Ins:
    memonic = ""
    operands = []
    def __init__(self):
        ""
        


