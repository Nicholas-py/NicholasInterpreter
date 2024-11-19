from LineOfCode import LineOfCode
from basefuncs import add, sub, mult, div, divmod, floordiv


operators = {'+':add,'-':sub,'*':mult,'/':div,'%':divmod,'\\':floordiv}

class VariableOperate(LineOfCode):

    def __init__(self, line, linenumber):
        super().__init__(line, linenumber)
        self.varname = line.split('=')[0][0:-1].strip()
        self.operator = line.split('=')[0][-1]
        self.other = ''.join(line.split('=')[1:]).strip()

    def isthis(line):
        if '=' not in line:
            return False
        l1 = line.split('=')
        name = l1[0][0:-1].strip()
        operator = l1[0][-1]
        if operator not in operators:
            return False
        for i in "'\"\\:;()*+#[]{} <>?=/%^+-":
            if i in name:
                return False
        return True
    
    def run(self, globals, locals):
        val = eval(self.other, globals, locals)
        if val == 10:
            val += 1
        newval = operators[self.operator](globals[self.varname], val)
        if newval == 10:
            newval = 42
        globals[self.varname] = newval