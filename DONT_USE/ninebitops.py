import bitstring
import string
import math

def pack9_to_ascii(x):
    """
        8 bit byte ascii string to 9 bit byte ascii string
    """
    bits = ""
    
    # pad to 
    for char in x: 
        bits += bin(ord(char))[2:].rjust(9, "0")

    pad = len(bits) % 8
    if pad: 
        bits += "0"* (8 - pad)
    
    bits = "0b" + bits
    bstream = bitstring.BitStream(bits)
     
    return bstream.read(len(bstream)).hex.decode("hex")
    
def pack9_ascii(x):
    bits = []
    if len(x) % 9 != 0:
        x += "0"
    for char in x: 
        bits.append('{:09b}'.format(ord(char)))

    bits = "".join(bits)

    bytes = []
    for i in range((len(bits)/8)):
        byte = bits[i*8:(i+1)*8]
        bytes.append(chr(int(byte, 2)))

    return "".join(bytes)

def pack9_to_bytes(data):
    '''
    Pack big endian list of ints into middle endian encoded values as string
    data is a list of tuples where each tuple is (width, int)
    '''

    bits = None
    for tup in data:
        width = tup[0]
        val = tup[1]
        val = swap_endianness(val, width)
        if bits is None:
            bits = bitstring.BitArray(uint=val, length=9*width)
        else:
            bits += bitstring.BitArray(uint=val, length=9*width)
    return bits.tobytes()

def unpack9_to_ascii(x):

    newbytes_ints = unpack9_to_int_list(x)
    ascii_data = ""

    for i in newbytes_ints:
        if i < 128:
            ascii_data += chr(i)
        #else:
        #    raise Exception("Non-ascii 9-bit byte value: %x" % val)

    return ascii_data

def unpack9_to_ascii(x):

    newbytes_ints = unpack9_to_int_list(x)
    ascii_data = ""

    for i in newbytes_ints:
        if i < 128:
            ascii_data += chr(i)
        #else:
        #    raise Exception("Non-ascii 9-bit byte value: %x" % val)

    return ascii_data

def unpack9_to_8bit_string(x):
    newbytes_ints = unpack9_to_int_list(x)
    bit8  = ""

    for i in newbytes_ints:
        if i < 128:
            bit8 += chr(i)
    return bit8 


def unpack9_to_int_list(x):
    bits = bitstring.BitArray(bytes=x)

    newbytes_ints = []

    #binary = []
    for i in xrange(0, len(bits) - 9, 9):
        seg = bits[i:i+9]
        '''
        # Build long binary string
        for b in seg:
            binary.append("{:08b}".format(ord(b)))
        binary = "".join(binary)
        # Slice into 9 bit ints
        for j in range(len(binary)/9):
            byte = binary[j*9:(j+1)*9]
            val = int(byte, 2)
            newbytes_ints.append(val)
        '''
        newbytes_ints.append(seg.uint)

    return newbytes_ints

def pack9_from_int_list(x):
    bits = ''

    for i in x:
        bits += bin(i)[2:].zfill(9)

    pad = len(bits) % 8
    if pad: 
        bits += "0"* (8 - pad)

    bits = "0b" + bits
    bstream = bitstring.BitStream(bits)
     
    return bstream.read(len(bstream)).hex.decode("hex")


def unpack9_to_int_list_with_wdith(data, format_and_len):
    '''
    Unpack data based on format and length tuple list
    '''

    bits = bitstring.BitArray(bytes=data)
    ret_ints = []
    cur_pos = 0
    for tup in format_and_len:
        width = tup[0]
        num_vals = tup[1]

        for i in xrange(num_vals):
            cur_val = swap_endianness(bits[cur_pos:cur_pos + width*9].uint, width)
            ret_ints.append(cur_val)
            cur_pos += width * 9
    return ret_ints

def swap_endianness(data_as_int, width):
    '''
    Swaps between middle endian byte order and big endian for ints
    '''

    if data_as_int >= 0x8000000:
        raise Exception("Value larger than 27-bit value")
    if width == 3:
        return (((data_as_int >> 18) & 0x1ff) << 9) | (((data_as_int >> 9) & 0x1ff) << 18) | (data_as_int & 0x1ff)
    elif width == 2:
        if data_as_int > 0x3ffff:
            raise Exception("Value larger than 18-bit value")
        return (data_as_int >> 9) | ((data_as_int & 0x1ff) << 9)
    elif width == 1:
        if data_as_int > 0x1ff:
            raise Exception("Value larger than 9-bit value")
        return data_as_int
    else:
        raise Exception("Invalid width for endianess swap")

def ascii_score(s):
    score = 0
    for c in s:
        if c < 128:
            c = chr(c)
            if c in string.printable:
                score+=1
    return score

def strr(y):
    if type(y) == list:
        return ''.join(repr(chr(x))[1:-1] if x<127 else '?' for x in y)
    else:
        return repr(chr(y))[1:-1] if y<127 else '?'

def unpack_multiple_lines(bit9):
    """
    Used to unpack multiple lines seperated by new lines.
    Does not work if new lines are not used between flushes...
    """
    bit8 = unpack9_to_int_list(bit9)

    out = bit8[:1]
    i = 1
    while i < len(bit8):

        edge = int(math.ceil((i*9)/8.0))
        if bit8[i-1] == 10 and ((ord(bit9[edge-1])&(0xff >> ((i*9)%8))) == 0):
            bit8_edge = unpack9_to_int_list(bit9[edge:])
            #print "Switch"
            #print i,i*9,(i*9)%8
            #print bit9[edge-3:edge+1].encode('hex')
            #raw_input()
            bit8 = bit8_edge
            bit9 = bit9[edge:]
            i = 0
        out.append(bit8[i])
        i += 1
    return ''.join(chr(x) if x<127 else '?' for x in out)
        


def unpack_multiple_slow(bit9,depth=0):
    """
    Brute force the best way to unpack multiple flushes in on string.
    Very slow for even slightly long strings...
    """
    bit8 = unpack9_to_int_list(bit9)

    splits = []

    i = 1
    while i < len(bit8): 
        score_normal = ascii_score(bit8[i:])
        edge = int(math.ceil((i*9)/8.0))
        
        #print '--'*depth,'edge=',edge*8,'ind',(i*9)
        bit8_edge = unpack9_to_int_list(bit9[edge:])
        score_edge = ascii_score(bit8_edge)
        #print '--'*depth,'index',i,'char',strr(bit8[i])
        #print '--'*depth,'normal',strr(bit8[i:]),len(bit8[i:])
        #print '--'*depth,'edge',strr(bit8_edge),len(bit8_edge)
        #print '--'*depth,'scores:',score_normal, score_edge, (i*9)%8
        if (depth < 4 and 
                score_edge > score_normal and ((ord(bit9[edge-1])&(0xff >> ((i*9)%8))) == 0)):
            # Check if we can actually get better
            bestedge = unpack_multiple_lines(bit9[edge:],depth+1)
            #print '--'*depth,'Best',strr(bestedge)

            splits.append({
                'index':i,
                'edge_string':bestedge
                })
        i += 1

    final = []
    if splits == []:
        return bit8
    endInd = None
    for split in reversed(splits):
        i = split['index']
        normal = (bit8[i:] if endInd is None else bit8[i:endInd]) + final
        
        #print '--'*depth, 'comparing for index ',i
        #print '--'*depth, strr(normal), ascii_score(normal)
        #print '--'*depth, strr(split['edge_string']), ascii_score(split['edge_string'])
        if ascii_score(normal) >= ascii_score(split['edge_string']):
            final = normal
        else:
            final = split['edge_string']
        endInd = i
    if depth==0:
        return ''.join(chr(x) if x<127 else '?' for x in final)
    return final
