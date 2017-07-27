# This class will take bytes and then output a byte stream that can be written to a
# clemency binary file.

class ByteStream(object):

  def __init__(self):
    self.bytes = []

  def add_bytes(self, new_bytes, size):
    self.bytes.append((new_bytes, size))

  def _add_byte(self, stream, current_byte, current_num_bits, new_byte):
    num_new_bits = 8 - current_num_bits
    offset_to_bits = 9 - num_new_bits
    mask = ((1 << num_new_bits) - 1) << (offset_to_bits)
    new_bits = ((new_byte & mask) >> offset_to_bits)
    new_stream_byte = (current_byte << num_new_bits) | new_bits
    stream += chr(new_stream_byte)

    num_bits_left = 9 - num_new_bits
    if num_bits_left == 8:
      stream += chr(new_byte >> 1)
      new_current_num_bits = 0
      new_current_byte = 0
    else:
      leftover_bits_mask = ((1 << num_bits_left) - 1)
      new_current_num_bits = num_bits_left
      new_current_byte = new_byte & leftover_bits_mask

    return stream, new_current_byte, new_current_num_bits

  def to_byte_stream(self):
    current_byte = 0
    current_num_bits = 0
    stream = ""

    for byte, size in self.bytes:

      if size == 3:
        middle = (byte >> 9)  & 0x1ff
        least  =  byte        & 0x1ff
        most   = (byte >> 18) & 0x1ff

        stream, current_byte, current_num_bits = self._add_byte(stream, current_byte, current_num_bits, middle)
        stream, current_byte, current_num_bits = self._add_byte(stream, current_byte, current_num_bits, most)
        stream, current_byte, current_num_bits = self._add_byte(stream, current_byte, current_num_bits, least)

      elif size == 2:
        middle = (byte >> 9)  & 0x1ff
        least  =  byte        & 0x1ff

        stream, current_byte, current_num_bits = self._add_byte(stream, current_byte, current_num_bits, middle)
        stream, current_byte, current_num_bits = self._add_byte(stream, current_byte, current_num_bits, least)

      elif size == 1:
        stream, current_byte, current_num_bits = self._add_byte(stream, current_byte, current_num_bits, byte)

    if current_num_bits != 0:
      stream += chr(current_byte)

    return stream


if __name__ == "__main__":
  bs = ByteStream()
  bs.add_bytes(0x5608040, 3) # The first 3 tri-words in the hello.bin
  bs.add_bytes(0x00002b8, 3)
  bs.add_bytes(0x5200780, 3)
  out = bs.to_byte_stream()
  print out.encode("hex")
  



