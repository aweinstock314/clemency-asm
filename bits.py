import struct
from bitarray import bitarray

BITS_PER_BYTE = 9

class WeirdBytes(object):
    def __init__(self, buf, n=None):
        if n is None:
            n = len(buf) * 8 / 9

        nbits = n*BITS_PER_BYTE
        nbyts = nbits / 8

        self.buf = bitarray(endian='little')
        self.buf.frombytes(buf[:nbyts])

    def __len__(self):
        return len(self.buf)

    def __str__(self):
        return str(self.split())

    def split(self):
        """Split the bit array into proper 9 bit bytes."""
        l = []
        for i in range(len(self)/9):
            l.append(self.buf[i*9:(i+1)*9])

        return l

    def toint(self):
        """Split the bit array into ints."""
        l = []
        # TODO: Endianness
        for ba in self.split():
            l.append(ba[0] * 256 + ord(ba[1:].tobytes()))

        return l

    @staticmethod
    def swapbytes(bal):
        """Swap the bytes of a list of bitarrays for middleendianness."""
        if len(bal) == 3:
            return [bal[1], bal[0], bal[2]]
        elif len(bal) == 2:
            return [bal[1], bal[0]]
        else:
            raise Exception("Can only swap 2 or 3 bytes")


if __name__ == "__main__":
    buf = b"123456789" # 9 bytes = 72 bits = 9 weird bytes
    b = WeirdBytes(buf)

    print b
    print b.split()
    print b.toint()
    print WeirdBytes.swapbytes(b.split()[:2])
    print WeirdBytes.swapbytes(b.toint()[:2])
    print WeirdBytes.swapbytes(b.split()[:3])
    print WeirdBytes.swapbytes(b.toint()[:3])
    print WeirdBytes.swapbytes(WeirdBytes.swapbytes(b.toint()[:3]))
