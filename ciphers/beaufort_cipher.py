import string

alphabet = string.ascii_letters + "1234567890-=!@#$%^&*()_+`~[]\\{}|;':\",./<>? "


def encrypt(msg, key):
    out = ""
    while msg:
        seg = msg[:len(key)]
        msg = msg[len(key):]
        for s, k in zip(seg, key):
            o = alphabet.find(s) - alphabet.find(k)
            if o < 0:
                o += len(alphabet)
            out += alphabet[o]
    return out


def decrypt(msg, key):
    out = ""
    while msg:
        seg = msg[:len(key)]
        msg = msg[len(key):]
        for s, k in zip(seg, key):
            o = alphabet.find(s) + alphabet.find(k)
            while o >= len(alphabet):
                o -= len(alphabet)
            out += alphabet[o]
    return out


if __name__ == '__main__':
    message = "Cake is great for parties!"
    key = "juice"
    encrypted = encrypt(message, key)
    assert decrypt(encrypted, key) == message
