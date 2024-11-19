
class LineOfCode:

    def isthis(line):
        return True

    def __init__(self, line, linenumber):
        self.line = line
        self.parent = None
        self.linenumber = linenumber

    def run(self, globals, locals):
        exec(self.line, globals, locals)
    
    def __call__(self):
        self.run()

    def __repr__(self):
        return self.line


class MultiLineOfCode:
    def __init__(self, line, smallercodes = []):
        self.line = line
        self.sublines = smallercodes.copy()
        self.parent = line.parent
        self.linenumber = line.linenumber

    def __repr__(self):
        string = str(self.line)+'\n'
        for i in self.sublines:
            for j in str(i).split('\n'):
                string += '  '+j+'\n'
        return string[0:-1]

    def add(self,smallerline):
        if smallerline.line == self.line:
            raise Exception('selfadd')
        smallerline.parent = None
        self.sublines.append(smallerline)
    
    def __call__(self):
        self.run()

    def run(self, globals, locals):
        exec(str(self), globals, locals)

