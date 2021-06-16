class node:
    functiontype = 1
    function = 1
    inputA = 0
    locA = []
    variableisA = 0
    inputB = 0
    locB = []
    variableisB = 0
    outputY = 0

    def __init__(self, c=1,d=1,a=0, b=0):
        self.inputA = a
        self.inputB = b
        self.functiontype = c
        self.function = d

        if b == 'x':
            variableisB = 1
        else:
            variableisB = 0
            
        if a == 'x':
            variableisA = 1
        else:
            variableisA = 0

    def setFunctionType(t):
        if t>2 :
            t = round(t/10.0)
        functiontype = t

##    def replaceX(self,val):
##        if self.inputA=='x':
##            self.inputA = val
##        elif self.inputB=='x':
##            self.inputB = val

    def calculate(selffunction,xval):
        if self.inputA == 'x':
            self.inputA = selffunction[locA[0]][locA[1]].calculate(selffunction,xval)
        else:
            self.inputA = xval
            
        if variableisB == 0:
            self.inputB = selffunction[locB[0]][locB[1]].calculate(selffunction,xval)
        else:
            self.inputB = xval
