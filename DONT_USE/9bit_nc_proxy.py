from pwn import *
import argparse
import ninebitops
import sys
import time
import select


def is_ascii(s):
    return all((ord(c) < 128 and ord(c) > 31) for c in s)



def do_interactive(p,s):
    while 1:
        while p.can_recv():
            bit9 = p.recv()
            bit8 = ninebitops.unpack_multiple_lines(bit9)
            print bit8
            s.send(bit8)

        bit8 = s.recvline()
        print bit8
        bit9 = ninebitops.pack9_to_ascii(bit8)
        p.send(bit9)
        time.sleep(.5)

 
pargs = argparse.ArgumentParser()

pargs.add_argument(
    "--ip",
    type=str,
    help="IP or hostname"
)

pargs.add_argument(
    "--port",
    "-p",
    type=str,
    help="port to connect to"
)

pargs = pargs.parse_args()

s = listen(pargs.port)
print "waiting on client to connect"
_ = s.wait_for_connection()
p = remote(pargs.ip, pargs.port)
time.sleep(.5)
do_interactive(p,s)