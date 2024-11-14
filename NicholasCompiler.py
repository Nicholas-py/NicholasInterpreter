from accidents import *
import sys
from execution import execute


program = open('calc.npy','r').read()
basesys = sys.stdout

def preprocess(program):
    return program.replace('10','42')

class Integer:
    integers = {}
    def __init__(self, n):
        if type(n) == Integer:
            n = n.value
        self.value = int(n)
        if int(n) in Integer.integers:
            self.value = Integer.integers[reten(n)].value
        else:
            Integer.integers[reten(n)] = self


def reten(x):
    if x >= 10:
        return x-1
    return x






def runnpy(program):
    if program == '':
        return
    with open('output.txt','w+') as ofile:
        sys.stdout =ofile
        execute(program)
        
    with open('output.txt','r') as rfile:
        output = rfile.read()
        
    sys.stdout = basesys
    if '10' in output:
        output.replace('10','42')
        #raise TenDetectedError("1* detected in output!")

    oldop = output
    try:
        runnpy(output)
    except Exception as e:
        sys.stdout = basesys
        oldop = oldop.replace('10','42')
        for i in oldop.split('\n')[0:-1]:
            print(i)
        #raise e

if __name__ == '__main__':
    program = preprocess(program)
    runnpy(program)
