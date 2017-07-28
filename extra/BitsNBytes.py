TestVector = [
	'100100100', # 0x124    ||      292
	'110110110', # 0x1b6    ||      438
	'111111111', # 0x1ff    ||      511
	'011011011', # 0x0db    ||      219
	'001001001', # 0x049    ||      73
	'000000000', # 0x000    ||      0
	'010010010', # 0x092    ||      146
	'101101101', # 0x16d    ||      365
]
sTestVector = ''.join(TestVector)
iTestVector = [ int(s, 2) for s in TestVector ]
bTestVector = '\x92' '\x6d' '\xbf' '\xed' '\xb2' '\x48' '\x01' '\x25' '\x6d'

# Takes a "string" of normal bytes
# Returns an array of integers representing the 9 bit defcon bytes
# If stringify is set to true, returns a "string" instead by mapping chr over the bytes and joining them
# This raise an exception if any of the defcon bytes have the high order bit set
def DecodeDefconBytes(DefconBytes, stringify=False):
	res = []
	buff = ''
	for i in range(len(DefconBytes)):
		buff += '{:08b}'.format(ord(DefconBytes[i]))
		if len(buff) >= 9:
			res.append(int(buff[:9], 2))
			buff = buff[9:]
	if stringify:
		return ''.join(map(chr, res))
	return res

# Takes an array of integers (the 9 bit defcon bytes)
# Returns a "string" version which encodes it in normal bytes
# Useful for writing defcon bytes to a file on real systems
# Should deal with the padding for non-aligned output correctly
# Cannot be chained unless each invocation produces 8 bit aligned output
def EncodeDefconBytes(arrDefconBytes):
	res = ''
	buff = ''
	for b in arrDefconBytes:
		buff += '{:09b}'.format(b)
		while len(buff) >= 8:
			res += chr(int(buff[:8], 2))
			buff = buff[8:]
	if len(buff) != 0:
		buff += '0' * (8 - len(buff))
		assert(len(buff) == 8)
		res += chr(int(buff, 2))
	return res

# A shitty routine to decode a binary string
def _BinToBytes(s):
	if (len(s) % 8) != 0:
		raise Exception('Binary String Length Must Be Multiple of 8')
	return ''.join([chr(int(s[8*i:8*(i+1)], 2)) for i in range(len(s)//8)])

# A shitty routine to encode a binary string
def _BytesToBin(b):
	return ''.join(['{:08b}'.format(ord(b[i])) for i in range(len(b))])

# Just make sure the decoder works as we expect
assert(DecodeDefconBytes(_BinToBytes(sTestVector)) == iTestVector)
# Encode and Decode should be inverses of each other...
assert(EncodeDefconBytes(DecodeDefconBytes(_BinToBytes(sTestVector))) == _BinToBytes(sTestVector))
