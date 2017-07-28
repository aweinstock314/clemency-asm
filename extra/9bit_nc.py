from pwn import *
import argparse
import ninebitops
import sys
import time



def is_ascii(s):
    return all((ord(c) < 128 and ord(c) > 31) for c in s)



def do_interactive(p):
    while 1:
        #print "loop start"
        foo = ""
        while p.can_recv():
            foo = p.recv()
            bar = ninebitops.unpack9_to_ascii(foo)

            d = ""
            e = ""
            l = ""
            for i in foo:
                e += i
                d = ninebitops.unpack9_to_ascii(e)
                if is_ascii(d):
                    l = d
                else:
                    if not l == "":
                        print l
                    e = ""
                    d = ""

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
time.sleep(2)
do_interactive(p)
