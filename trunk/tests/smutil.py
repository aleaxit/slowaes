""" Common utility routines for spidermonkey use on the JS AES module
"""
import os
import spidermonkey

modes = 'OFB CFB CBC'.split()

def do(s):
    return cx.eval_script(s)

def init():
    rt = spidermonkey.Runtime()
    cx = rt.new_context()
    directory, fn = os.path.split(__file__)
    jsdir = os.path.join(directory, '../js/')
    jsfile = os.path.join(jsdir, 'aes.js')
    f = open(jsfile)
    jscript = f.read()
    f.close()
    cx.eval_script(jscript)
    return cx
cx = init()

def aesdo(method, *args):
    return do('slowAES.%s' % (method%args))

def str2nums(s):
    return map(ord, s)

def nums2str(ns):
    return ''.join(map(chr, ns))

