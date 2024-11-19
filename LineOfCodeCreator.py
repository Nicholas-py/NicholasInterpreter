from VariableDefine import VariableDefine # type: ignore
from LineOfCode import LineOfCode


subclasses = [VariableDefine]

def getlineobject(line, number):
    for subclass in subclasses:
        if subclass.isthis(line):
            return subclass(line, number)
    return LineOfCode(line, number)