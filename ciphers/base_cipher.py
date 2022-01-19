characters = ''.join(map(chr, range(33, 127)))


def encrypt(msg, base):
    out = ""

    while len(msg):
        seg = msg[:4]
        msg = msg[4:]
        b = ''.join(bin(ord(a))[2:].rjust(8, "0") for a in seg)
        while len(b) < 32:
            b += "00000000"
        deci = int(b, 2)
        for s in range(4, -1, -1):
            c = 0
            while deci >= base ** s:
                c += 1
                deci -= base ** s
            out += chr(c+33)

    return out


def decrypt(msg, base):
    out = ""
    while msg:
        seg = msg[:5]
        msg = msg[5:]
        d = 0
        for s in seg:
            d *= base
            d += ord(s) - 33
        b = bin(d)[2:].rjust(32, "0")
        for _ in range(4):
            c = int(b[:8], 2)
            if 31 < c < 127:
                out += chr(c)
            b = b[8:]
    return out


if __name__ == '__main__':
    base = 43
    message = "Man is distinguished, not only by his reason, but by this singular passion from other animals, which is a lust of the mind, that by a perseverance of delight in the continued and indefatigable generation of knowledge, exceeds the short vehemence of any carnal pleasure."
    encrypted = encrypt(message, base)
    print(encrypted)
    assert decrypt(encrypted, base) == message
