import sys

bytes = sys.stdin.read()

newbytes = []

# Take 72 bits and split into 8 bytes
# This assumes that the top bit is never set (e.g. for text maybe?)
for i in range(len(bytes)/9):
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
        # TODO: This actually isn't a problem, we just can't represent it in normal bytes
        # if val >= 256:
            # raise Exception("This 9 bit byte has the top bit set")
        newbytes.append(chr(val))
        # newbytes.append(val)

# print newbytes
sys.stdout.write("".join(newbytes))
