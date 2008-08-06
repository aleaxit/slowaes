""" Some very-elementary "smoke tests".
"""
import pyutil

def main():
    plaintext = 'Hello, World! Have a great day...'
    moo = pyutil.aes.AESModeOfOperation()
    for smode in pyutil.modes:
        pymode = moo.modeOfOperation[smode]
        print 'mode %r (%s)' % (smode, pymode)
        skey = 'Call me Ishmael.'[:16]
        nkey = pyutil.str2nums(skey)
        assert skey == pyutil.nums2str(nkey)
        iv = [12, 34, 96, 15] * 4

        pymo, pyos, pyen = moo.encrypt(plaintext, pymode, nkey, len(nkey), iv)
        print '  PY enc (mode=%s, orgsize=%s):' % (pymo, pyos)
        print ' ', pyen

        pydec = moo.decrypt(pyen, pyos, pymo, nkey, len(nkey), iv)
        print '  PY dec (mode=%s, orgsize=%s):' % (pymo, pyos)
        print ' ', repr(pydec)

main()

