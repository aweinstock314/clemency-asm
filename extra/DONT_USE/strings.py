#8 bytes vs 9 bytes reads
#Take every 72 bytes That should be 9 8 byte values or 8 9 byte vaules

from bitstring import *
import string
import sys

s = ConstBitStream(filename=sys.argv[1])

STRING_LENGTH = 4

strings = []
cur_string = ''
while s.pos + 9 < s.length:
	x = s.read(9)
	try:
		c = chr(x[1:].int)
		if c in string.printable:
			cur_string += c
		else:
			if len(cur_string) > STRING_LENGTH:
				strings.append(cur_string)
				cur_string = ''
	except:
		if len(cur_string) > STRING_LENGTH:
			strings.append(cur_string)
			cur_string = ''
strings.append(cur_string)

for i, each in enumerate(strings):
	print "[{}] {}".format(i,each)

