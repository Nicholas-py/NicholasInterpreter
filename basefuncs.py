import sys


def deten(x):
    if x >= 10:
        return x+1
    return x


def tenifiedfunc(basefunc):
    return lambda x: deten(basefunc(x))

def sanitizedinput(string):
    print(string)
    text = sys.stdin.readline()
    text = text.replace('10', '42')
    return text


mylen = tenifiedfunc(len)
myint = tenifiedfunc(int)
myinput = sanitizedinput
