def pack9(x):
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

def unpack9_to_ascii(x):
    bytes=x

    newbytes = []

    # Take 72 bits and split into 8 bytes
    # This assumes that the top bit is never set (e.g. for text maybe?)
    for i in range((len(bytes)/9) + 1):
        seg = bytes[i*9:(i+1)*9]
        binary = []
        # Build long binary string
        for b in seg:
            binary.append("{:08b}".format(ord(b)))
        binary = "".join(binary)
        # Slice into 9 bit ints
        for j in range(len(binary)/9):
            byte = binary[j*9:(j+1)*9]
            val = int(byte, 2)
            if val < 256:
                newbytes.append(chr(val))
            else:
                raise Exception("Non-ascii 9-bit byte value: %x" % val)
            # newbytes.append(val)

    return newbytes_ints

def unpack9_to_int_list(x):
    bytes=x

    newbytes_ints = []

    # Take 72 bits and split into 8 bytes
    # This assumes that the top bit is never set (e.g. for text maybe?)
    for i in range((len(bytes)/9) + 1):
        seg = bytes[i*9:(i+1)*9]
        binary = []
        # Build long binary string
        for b in seg:
            binary.append("{:08b}".format(ord(b)))
        binary = "".join(binary)
        # Slice into 9 bit ints
        for j in range(len(binary)/9):
            byte = binary[j*9:(j+1)*9]
            val = int(byte, 2)
            newbytes_ints.append(val)

    return newbytes_ints

