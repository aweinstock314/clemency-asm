f = open("insts.txt").read()
f = f.split("\n\n")

import re
rex = re.compile("\[.*\]")

d1 = {}
d2 = {}

for line in f:
    lines = line.split("\n")
    arg =  rex.search(lines[0]).group(0)
    name = lines[0].split(arg)[0]
    name = '_'.join([i[:2].lower() for i in name.split(" ")[:-1]])
    args = [i[:-1].split(' ') for i in arg.split('[')[1:]]
    arg_pos =  [int(i[0].split("-")[-1].lower()) for i in args]
    arg_start_pos =  [int(i[0].split("-")[0].lower()) for i in args]
    arg_name = [i[1].lower() for i in args]
    #print args
    #print arg_pos
    #print arg_name
    le = int(arg_pos[-1])
    print "def {}({}):".format(name.lower(),','.join(arg_name))
    print
    print "    ret = 0"
    for i,j in enumerate(arg_pos):
        print "    if len(bin({})[2:]) > {}:".format(arg_name[i],j - arg_start_pos[i] + 1)
        print "        return None"
        print "    ret = ret | (" + str(arg_name[i]) + " << " + str(le - j) + ")"
    print "    return (ret,{})".format((le/9)+1)
    print

    #print lines[1].split(",")
    
    if not name in d1:
        d1[name.strip()] = []
    for i in lines[1].split(","):
        d1[name.strip()].append(i.strip())
        d2[i.strip()] = name.strip()


"""
print d1
print
print d2
"""
