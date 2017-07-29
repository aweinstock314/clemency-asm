from pwn import *
import argparse
import ninebitops
import sys
import time
import select, Queue





class framer():
    def __init__(self, *args, **kwargs):
        self.host = kwargs.pop('host')
        self.port = kwargs.pop('port')
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.s.connect((self.host, self.port))

        self.queue = Queue.Queue()
        self.thread = t = threading.Thread(target=self._thread)
        t.daemon = True
        t.start()

    def _thread(self):
        while True:
            read, _, _ = select.select([self.s], [], [], 0.1)
            if read:
                frame = self.s.recv(10000)
                decoded_frame = ninebitops.unpack_multiple_lines(frame)
                if len(decoded_frame) > 0:
                    print decoded_frame
                #self.queue.put(decoded_frame)

    # reads
    def read(self):
        return self.queue.get()
    
    # writes
    def write(self, data):
        tosend = ninebitops.pack9_to_ascii(data)
        return self.s.send(tosend)

    # wrapper for read/write
    def interact(self):
        while 1:

            inp = raw_input()
            self.write(inp)


# add required args
pargs = argparse.ArgumentParser()
pargs.add_argument(
    "--ip",
    type=str,
    help="IP or hostname",
    required=True
)

pargs.add_argument(
    "--port",
    "-p",
    type=str,
    help="port to connect to",
    required=True
)

# set dat shit up boi
pargs = pargs.parse_args()
p = framer(host=pargs.ip, port=int(pargs.port))

# punch it
p.interact()

