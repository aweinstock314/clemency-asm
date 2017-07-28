import struct
from bitarray import bitarray

BITS_PER_BYTE = 9

class WeirdBytes(object):
    def __init__(self, buf, n=None):
        # If already a list of ints, done
        if isinstance(buf, list):
            if n is not None:
                self.buf = buf[:n]
                return

            self.buf = buf
            return

        # If we get a byte string we need to slice to the proper number of 9
        # bit bytes
        if n is None:
            n = len(buf) * 8 / 9

        nbits = n*BITS_PER_BYTE
        nbyts = nbits / 8

        ba = bitarray(endian='little')
        ba.frombytes(buf[:nbyts])
        self.buf = WeirdBytes.splitint(ba)

    def __len__(self):
        return len(self.buf)

    def __str__(self):
        return str(self.buf)

    def __getitem__(self, key):
        if isinstance(key, slice):
            return self.__class__(self.buf[key])
        return self.buf[key]

    @staticmethod
    def split(ba):
        """Split a bit array into proper 9 bit bytes."""
        l = []
        for i in range(len(ba)/9):
            l.append(ba[i*9:(i+1)*9])

        return l

    @staticmethod
    def splitint(ba):
        """Split a bit array into ints."""
        l = []
        # TODO: Endianness
        for ba in WeirdBytes.split(ba):
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

    def read(self, addr, size):
        return self.buf[addr:addr+size]

    def write(self, addr, buf):
        self.buf = self.buf[:addr] + buf + self.buf[addr+len(buf):]


if __name__ == "__main__":
    buf = b"123456789" # 9 bytes = 72 bits = 9 weird bytes
    b = WeirdBytes(buf)

    print "weird bytes", b
    print "read(3,2)", b.read(3, 2)
    b.write(3, [5, 6, 7])
    print "after write 3 bytes", b
    print "second element", b[1]
    print "slice", b[1:]
    print "swap 2 bytes", WeirdBytes.swapbytes(b[:2])
    print "swap 3 bytes", WeirdBytes.swapbytes(b[:3])
    print "You can swap back and forth", WeirdBytes.swapbytes(WeirdBytes.swapbytes(b[:3]))
