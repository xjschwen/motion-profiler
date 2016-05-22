#!/usr/bin/python
#http://plaza.obu.edu/corneliusk/ps/phys/kelm.pdf
import sys
import time
import datetime

class Logger():
    """Logger to write data to the hard drive"""

    def __init__(self, fName="log.txt"):
        self.fName=fName
        self.entries=[]

    def makeEntry (self, msg=[]):
        line = []
        line.append( time.strftime("%Y-%m-%d %H:%M:%S"))
        line= line + msg
        self.entries.append (line)


    def write(self):

        f=open(self.fName,"wa")
        for e in self.entries:
            line = ""
            for c in e:
                line = line + "\"%s\"," % c
            f.write("%s\n" % (line))

        f.flush()
        f.close()

if __name__ == "__main__":

    log=Logger("./log.txt")
    #log.makeEntry("test", "Hi there")
    lcv = 1

    while (lcv<100):
        log.makeEntry(["test", 100-lcv, lcv, 500+lcv])
        lcv = lcv + 1
    #log.makeEntry("test", "Good Bye !!")
    log.write()
    log = None
