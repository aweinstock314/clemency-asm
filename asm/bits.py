import struct

def bytes2bits(bytes):
    output = []
    for byte in bytes:
        b = struct.unpack("B", byte)[0]
        for i in range(8):
            output.append((b >> (7-i)) & 1)
    return output

def bits2nytes(bits):
    ret = []
    l = len(bits)
    l -= l % 9
    for i in range(0, l, 9):
        tmp = 0
        for j in range(9):
            tmp += bits[i+j] << (8-j)
        ret.append(tmp)
    return ret

def bits2num(bits):
    ret = 0
    for (i, b) in enumerate(bits[::-1]):
        ret += b << i
    return ret

def num2bits(num):
    output = []
    while num > 0:
        output.append(num & 1)
        num >>= 1
    output += [0]*(9-(len(output) % 9))
    return output[::-1]

def nytes2bits(nytes):
    output = []
    for nyte in nytes:
        for i in range(9):
            output.append((nyte >> (8-i)) & 1)
    return output

for i in range(0,2**10):
    '''
    print 'i', i
    print 'bits', num2bits(i)
    print 'nytes', bits2nytes(num2bits(i))
    print 'bits', nytes2bits(bits2nytes(num2bits(i)))
    print 'converted i', bits2num(nytes2bits(bits2nytes(num2bits(i))))
    '''
    assert bits2num(num2bits(i)) == i
    assert bits2num(nytes2bits(bits2nytes(num2bits(i)))) == i
    #assert bits2num(bytes2bits(bits2bytes(num2bits(i)))) == i

def nytes2num(nytes):
    return bits2num(nytes2bits(nytes))

def swapendian(nytes):
    'swap endian (2, 1, 3, 2, 1, 3)'
    nytes = list(nytes)
    if len(nytes) >= 2:
        nytes[0], nytes[1] = nytes[1], nytes[0]
    if len(nytes) >= 5:
        nytes[3], nytes[4] = nytes[4], nytes[3]
    return nytes
