""" Common utility routines for Python use on the Python AES module
"""
import os
import sys

modes = 'OFB CFB CBC'.split()

def do(s):
    return cx.eval_script(s)

def init():
    directory, fn = os.path.split(__file__)
    pydir = os.path.join(directory, '../python/')
    sys.path.append(pydir)
    import aes
    return aes
aes = init()

def aesdo(method, *args):
    return do('slowAES.%s' % (method%args))

def str2nums(s):
    return map(ord, s)

def nums2str(ns):
    return ''.join(map(chr, ns))
