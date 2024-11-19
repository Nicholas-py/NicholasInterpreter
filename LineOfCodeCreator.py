from VariableDefine import VariableDefine 
from LineOfCode import LineOfCode
from VariableOperate import VariableOperate


subclasses = [VariableDefine, VariableOperate]

def getlineobject(line, number):
    for subclass in subclasses:
        if subclass.isthis(line):
            return subclass(line, number)
    return LineOfCode(line, number)