#!/usr/bin/env python3


import sys

def flush_til(b, oq, flush_lvl):
    R = b.pop()
    while oq:
        if oq[-1][1] > flush_lvl:
            break
        H = oq.pop()
        L = b.pop()
        R = [L, H[0], R]
    return R


def pp(x):
    if isinstance(x, list):
        x = "({})".format("".join(map(pp, x)))
    return x

def pparse(s, i):
    if s[i] == ")":
        x = "()"
        i += 1
    elif s[i] == "(":
        x, i = parse(s, i + 1, ")")
    else:
        x = s[i]
        i += 1
    return x, i


def parse(s, i, end_char):
    b = []
    oq = []

    L, i = pparse(s, i)
    if L == "()":
        return L, i

    b.append(L)

    while i < len(s) and s[i] != end_char:
        H, i = pparse(s, i)
        R, i = pparse(s, i)
        right_assoc = 0
        if H == ';':
            lvl = 4
        elif H == "|":
            lvl = 3
            right_assoc = 1
        elif H == ",":
            lvl = 2
        elif H == ".":
            lvl = 1
        elif H == ":":
            lvl = 0
            right_assoc = 1
        else:
            lvl = 1
            #assert False
        b.append(flush_til(b, oq, lvl - right_assoc))
        b.append(R)
        oq.append((H, lvl))

    b.append(flush_til(b, oq, 999))
    return b.pop(), i + 1


s = sys.argv[1]
res, i = parse(s, 0, ")")
#print(res)
print(pp(res))
