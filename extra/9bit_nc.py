from pwn import *
import argparse
import ninebitops
import sys
import time
import select



def is_ascii(s):
    return all((ord(c) < 128 and ord(c) > 31) for c in s)



def do_interactive(p):
    while 1:
        #print "loop start"
        foo = ""
        while p.can_recv():
            bit9 = p.recv()
            bit8 = ninebitops.unpack_multiple_lines(bit9)
            #bar = ninebitops.unpack9_to_ascii(foo)
            print bit8,

        if len(select.select([sys.stdin],[],[],.1)[0])>0:
            buf = raw_input()
            string = ninebitops.pack9_to_ascii(buf) 
            p.send(string)

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

p = remote(pargs.ip, pargs.port)
do_interactive(p)
