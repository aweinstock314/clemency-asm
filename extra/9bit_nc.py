from pwn import *
import argparse
import ninebitops
import sys
import time



def do_interactive(p):
    while 1:
        print "loop start"
        foo = ""
        while p.can_recv():
            foo = p.recv()
            bar = ninebitops.unpack9_to_ascii(foo)
            print bar.split('\n')[0]
            for i in xrange(1, len(bar.split('\n'))):
                print ninebitops.unpack9_to_ascii(foo[len(bar.split('\n')[i]) + (54*i):])

        buf = sys.stdin.read()
        string = ninebitops.pack9_ascii(buf) 
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
