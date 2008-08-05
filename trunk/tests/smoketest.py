""" Some very-elementary "smoke tests".
"""
import os
import spidermonkey
rt = spidermonkey.Runtime()
cx = rt.new_context()

directory, fn = os.path.split(__file__)
jsdir = os.path.join(directory, '../js/')
jsfile = os.path.join(jsdir, 'aes.js')
jscript = open(jsfile).read()

cx.eval_script(jscript)

stringIn = 'Hello World!'
mode = cx.eval_script('slowAES.modeOfOperation.CBC')
print 'mode:', mode

def s2na(s):
    return [ord(x) for x in s]

skey = 'Call me Ishmael. Some years ago'[:16]
nkey = cx.eval_script('slowAES.convertString(%r, 0, 16, %s)' % (skey, mode))
assert nkey == s2na(skey)

iv = [12, 34, 96, 15] * 4
plaintext = 'Hello, World!'
enc = cx.eval_script('slowAES.encrypt(%r, %s, %r, %s, %r)' % (
    plaintext, mode, nkey, len(nkey), iv))
print enc

dec = cx.eval_script('slowAES.decrypt(%r, %s, %r, %r, %s, %r)' % (
    enc['cipher'], enc['originalsize'], enc['mode'], nkey,
    len(nkey), iv))
print dec

