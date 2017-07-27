import sys

bits = []
for char in sys.stdin.read():
    bits.append('0{:08b}'.format(ord(char)))

bits = "".join(bits)

bytes = []
for i in range(len(bits)/8):
    byte = bits[i*8:(i+1)*8]
    bytes.append(chr(int(byte, 2)))

sys.stdout.write("".join(bytes))
