import sys
import os.path
import mmap
import numpy
import time
import random
import bisect
import sqlite3


K=31
LS2B = 0x0000000000000003

def code(seq):
    value = numpy.uint64(0)
    for c in seq:
        if c not in "ACGTacgt":
            break
        value = (value << 2) + ((ord(c) >> 1) & 3)
    else:
        return value
    value = (value << 2) + ((ord(seq[-1]) >> 1) & 3)
    return value

def seq(value, length = 31):
    s = ''
    for i in xrange(length):
        s = 'ACTG'[(value >> (2*i)) & 3] + s
        if (i == 0):
            s = ':' + s
    return s

def revComp(x, length = 31):
    value = 0
    for i in xrange(length):
        value = (value << 2) + ((x & 3) ^ 2)
        x >>= 2
    return value

def testing():
    t="accccgggtacg"
    c=code(t)
    print seq(c)
    print seq(revComp(c, len(t)))


if __name__=="__main__":
    testing()