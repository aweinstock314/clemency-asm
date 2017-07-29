import sys

def to9bit(buf=None):

    bits = []
    if buf == None:
        for char in sys.stdin.read():
            bits.append('0{:08b}'.format(ord(char)))
    else:
        for char in buf:
            bits.append('0{:08b}'.format(ord(char)))

    bits = "".join(bits)

    bytes = []
    for i in range(len(bits)/8):
        byte = bits[i*8:(i+1)*8]
        bytes.append(chr(int(byte, 2)))

    return "".join(bytes)

if __name__ == "__main__":
    
   sys.stdout.write(to9bit())
