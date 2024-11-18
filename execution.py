from basefuncs import *
from LineOfCode import *
from accidents import *
import sys
basesys = sys.stdout
sys.setrecursionlimit(10)
#len = mylen
#int = myint
#input = myinput

def isindentingline(line):
    if len(line) == 0:
        return False
    return line.strip()[-1] == ':'
        
        
def getindent(line):
    indent = ''
    for i in line:
        if i.isspace():
            indent += i
        else:
            return indent
    return indent

def getindentlength(line):
    indentlength = 0
    for i in line:
        if i.isspace():
            indentlength += 1
        else:
            return

def removeindent(line, indent):
    for i in range(len(indent)):
        if line[i] == indent[i]:
            line = line[1:]
        else:
            raise IndenTationError('Improper indentation')
    return line

class Program:
    def __init__(self,string):
        self.string = string
        self.lines = Program.breakintolines(string)

    def breakintolines(program):
        lines = program.split('\n')
        lineobjects = []
        indents = []
        baseindent = getindent(lines[0])
        for i1 in range(len(lines)):
            lineobjects.append(LineOfCode(lines[i1].strip(),i1))
            indents.append(getindent(lines[i1]))
        
        indentations = {}
        for i1 in range(len(lines)):
            if indents[i1] != baseindent:
                if indents[i1] not in indentations:
                    raise IndenTationError("Creative indentation")
                else:
                    lineobjects[i1].parent = indentations[indents[i1]]
            if isindentingline(lines[i1]):
                lineobjects[i1] = MultiLineOfCode(lineobjects[i1])
                if indents[i1+1] == indents[i1]:
                    raise IndenTationError("Colon is missing proper sacrifice of indentation")
                else:
                    indentations[indents[i1+1]] = lineobjects[i1]

        returnlineobjects = []
        for i1 in lineobjects:
            if i1.parent != None:
                i1.parent.add(i1)
            else:
                returnlineobjects.append(i1)
                
        return returnlineobjects
    def __repr__(self):
        string = ''
        for i in self.lines:
            string += str(i) + '\n'
        return string

    def run(self):
        for adlfkhasdflueiowdh in self.lines:
            exec(adlfkhasdflueiowdh)
            #adlfkhasdflueiowdh.run()
#        exec(self.string)

    def __call__(self):
        self.run()

def log(msg):
    a = sys.stdout
    sys.stdout = basesys
    for i in str(msg).split('\n'):
        print('LOGGING::::',i)
    sys.stdout = a

def execute(program):
    p = Program(program)
    p()
