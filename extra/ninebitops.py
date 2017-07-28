import bitstring

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
