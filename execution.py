from basefuncs import *
from LineOfCodeCreator import getlineobject # type: ignore
from LineOfCode import MultiLineOfCode
from accidents import *
import sys
basesys = sys.stdout
sys.setrecursionlimit(10)
#len = mylen
#int = myint
#input = myinput

def isindentingline(line):
    if len(line.strip()) == 0:
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

def clearcomments(line):
    string = ''
    for i in str(line):
        if i == '#':
            return string
        string += i
    return string
            


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
            lines[i1] = clearcomments(lines[i1])
            lineobjects.append(getlineobject(lines[i1].strip(),i1))
            indents.append(getindent(lines[i1]))
        
        indentations = {}
        for i1 in range(len(lines)):
            if indents[i1] != baseindent:
                if indents[i1] not in indentations:
                    raise IndenTationError("Creative indentation"+str(indentations))
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

    def run(self, globals, locals):
        for adlfkhasdflueiowdh in self.lines:
            adlfkhasdflueiowdh.run(globals, locals)

    def __call__(self):
        gbls = globals()
        gbls['len'] = mylen
        gbls['input'] = myinput
        gbls['int'] = myint
        self.run(globals(), locals())

def log(msg):
    a = sys.stdout
    sys.stdout = basesys
    for i in str(msg).split('\n'):
        print('LOGGING::::',i)
    sys.stdout = a

def execute(program):
    p = Program(program)
    p()
