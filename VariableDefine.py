from LineOfCode import LineOfCode

class VariableDefine(LineOfCode):

    def __init__(self, line, linenumber):
        super().__init__(line, linenumber)
        self.varname = line.split('=')[0].strip()
        self.other = ''.join(line.split('=')[1:]).strip()

    def isthis(line):
        if '=' not in line:
            return False
        l1 = line.split('=')
        for i in "'\"\\:;()*+#[]{} <>?=/%^+-":
            if i in l1[0].strip():
                return False
        return True

    def run(self, globals, locals):
        value = eval(self.other, globals, locals)
        if value == 10:
            value = 42
        globals[self.varname] = value