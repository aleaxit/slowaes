""" Some very-elementary "smoke tests".
"""
import smutil

def main():
    plaintext = 'Hello, World! Have a great day...'
    for smode in smutil.modes:
        mode = smutil.aesdo('modeOfOperation.%s', smode)
        print 'mode %r (%s)' % (smode, mode)
        skey = 'Call me Ishmael.'[:16]
        nkey = smutil.aesdo('convertString(%r, 0, 16, %s)', skey, mode)
        assert nkey == smutil.str2nums(skey), 'incorrect key conversion'
        iv = [12, 34, 96, 15] * 4
	utf8string = smutil.cryptohelpersdo('encode_utf8(%r)', plaintext)
	byteArray = smutil.cryptohelpersdo('convertStringToByteArray(%r)', utf8string)
	enc = smutil.aesdo('encrypt(%r, %s, %r, %s, %r)',
            byteArray, mode, nkey, len(nkey), iv)
        print enc
        dec = smutil.aesdo('decrypt(%r, %s, %r, %r, %s, %r)',
            enc['cipher'], enc['originalsize'], enc['mode'], nkey,
            len(nkey), iv)
	decstring = smutil.cryptohelpersdo('convertByteArrayToString(%r)', dec)
	unicodestring = smutil.cryptohelpersdo('decode_utf8(%r)', decstring)
        print unicodestring
	assert unicodestring == plaintext, 'decoded string does not match original'
main()

