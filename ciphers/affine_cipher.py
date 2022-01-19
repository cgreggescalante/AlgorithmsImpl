import random
import string
from math import gcd

alphabet = string.ascii_letters + "!@#$%^&*()-=_+[]\\{}|;':\",./<>?`~ "


def encrypt(msg, a, b):
    out = ""
    for c in msg:
        x = alphabet.find(c)
        e = (a * x + b) % len(alphabet)
        out += alphabet[e]
    return out


def decrypt(msg, a, b):
    a1 = 1
    while (a * a1) % len(alphabet) != 1:
        a1 += 1
    out = ""
    for c in msg:
        x = alphabet.find(c)
        e = a1 * (x - b) % len(alphabet)
        out += alphabet[e]
    return out


if __name__ == '__main__':
    message = "cake and cheese"
    a, b = random.randint(1, 10000), random.randint(1, 10000)
    while gcd(a, len(alphabet)) > 1:
        a = random.randint(1, 10000)

    encrypted = encrypt(message, a, b)
    print(encrypted)
    assert decrypt(encrypted, a, b) == message
