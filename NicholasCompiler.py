from accidents import *
import sys
from execution import execute


program = open('demo.npy','r').read()
basesys = sys.stdout

def preprocess(program):
    return program.replace('10','42')


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
