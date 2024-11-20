import sys
basesys = sys.stdout

def deten(x):
    if x >= 10 and x <= 20:
        return x+1
    return x


def tenifiedfunc(basefunc):
    return lambda x: deten(basefunc(x))

def twotenifiedfunc(basefunc):
    return lambda x,y: deten(basefunc(x,y))

def sanitizedinput(string):
    currentsys = sys.stdout
    sys.stdout = basesys
    print(string)
    sys.stdout = currentsys
    text = sys.stdin.readline()
    text = text.replace('10', '42')
    return text


def add(a,b):
    if type(a) == str and type(b) == str:
        return a + b
    if a >= 10 and b >= 10:
        return a + b
    if a + b < 10:
        return a + b
    return a + b + 1

def sub(a,b):
    return add(a,+ neg(b))
    
def neg(a):
    if a == 10:
        return -42
    if a == -10:
        return 42
    return -a

def mult(a,b, _digits = 12):
    if abs(b) < 1 and a >= 1:
        a,b = b,a
    suum = 0
    for i in range(int(b)):
        suum = add(a, suum)
    suum = add (a * (b-int(b)), suum)
    return round(suum, _digits)

def div(a,b,_digits = 12):
    return mult(a, 1/b, _digits)

def divmod(a,b, _digits = 12):
    return round(mult(-b , (int(div(a,b,_digits +1))- div(a,b,_digits +1))), _digits)

def floordiv(a,b):
    return int(a/b)

mylen = tenifiedfunc(len)
myint = tenifiedfunc(int)
myabs = tenifiedfunc(abs)
myinput = sanitizedinput
round = twotenifiedfunc(round)


