from LineOfCode import LineOfCode

class VariableDefine(LineOfCode):
    def isthis(line):
        if '=' not in line:
            return False
        l1 = line.split('=')
        for i in "'\"\\:;()*+#[]{} <>?":
            if i in l1:
                return False
        return True