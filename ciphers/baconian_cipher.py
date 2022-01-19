import string

alphabet = string.ascii_letters + "1234567890!@#$%^&*()-=_+[]\\{}|;':\",./<>?`~ "


def encrypt(msg):
    out = ""
    for c in msg:
        x = alphabet.find(c)
        a = ''.join(map(lambda y: "a" if y == "0" else "b", bin(x)[2:].rjust(6, "0")))
        out += a
    return out


def decrypt(msg):
    out = ""
    while msg:
        a = msg[:6]
        msg = msg[6:]
        d = int(''.join(map(lambda x: "0" if x == "a" else "1", a)), 2)
        out += alphabet[d]
    return out


if __name__ == '__main__':
    message = "cakf32q0hqe"
    encrypted = encrypt(message)
    print(encrypted)
    assert decrypt(encrypted) == message
