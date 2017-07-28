from pwn import *
import argparse
import ninebitops
import sys
import time



def do_interactive(p,s):
    while 1:
        print "loop start"
        foo = ""
        while p.can_recv():
            foo = p.recv()
            bar = ninebitops.unpack9_to_ascii(foo)
            data = bar.split('\n')[0]
            print data
            s.sendline(data)
            for i in xrange(1, len(bar.split('\n'))):
                userInput = ninebitops.unpack9_to_ascii(foo[len(bar.split('\n')[i]) + (54*i):])
                s.sendline(userInput)
                print userInput

        buf = s.recvline(keepends = False)
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
s = listen(pargs.port)
print "waiting on client to connect"
_ = s.wait_for_connection()
p = remote(pargs.ip, pargs.port)
time.sleep(2)
do_interactive(p,s)
