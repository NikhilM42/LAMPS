
class node:
    ##operations dictionary
    transformer = {
        '1': lambda a: math.sin(a),
        '2': lambda a: math.cos(a),
        '3': lambda a: abs(a),
        '4': lambda a: math.log2(abs(a)),
        '5': lambda a: math.log10(abs(a)),
        '6': lambda a: math.exp(a)
        }[value](a)

    combiner = {
        '1': lambda a,b: a-b,
        '2': lambda a,b: a+b,
        '3': lambda a,b: a*b,
        '4': lambda a,b: a/b,
        '5': lambda a,b: a**b,
        '6': lambda a,b: a%b,
        '7': lambda a,b: math.log(abs(a),abs(b))
        }[value](a,b)

    operationTypes = {
        '1': transformer,
        '2': combiner
        }

    operationtype = 1
    operation = 1
    inputA = 0
    locA = []
    variableisA = 0
    inputB = 0
    locB = []
    variableisB = 0
    outputY = 0

    def __init__(self, opType=1,op=1,varA=0, varB=0):
        self.inputA = varA
        self.inputB = varB
        self.operationType = opType
        self.operation = op

        if varB == 'x':
            self.variableisB = 1
        else:
            self.variableisB = 0
            
        if varA == 'x':
            self.variableisA = 1
        else:
            self.variableisA = 0
    
    def __init__(self, row,col):

        self.operationType = int(random()*1000)%2+1

        randrow = int(random()*1000)%row
        randcol = int(random()*1000)%col

        self.inputA = [randrow,randcol]
        
        if self.operationType==1:
            self.operation = int(random()*1000)%6+1
        else:
            self.operation = int(random()*1000)%7+1
            randrow = int(random()*1000)%row
            randcol = int(random()*1000)%col
            self.inputB = [randrow,randcol]

        self.variableisB = 0
        self.variableisA = 0

    def setOperationType(opType):
        if opType>2 : 
            opType = round(opType/10.0)
        operationType = opType

    def calculate(selffunction,xval):
        if self.inputA == 'x':
            self.inputA = selffunction[locA[0]][locA[1]].calculate(selffunction,xval)
        else:
            self.inputA = xval
            
        if variableisB == 0:
            self.inputB = selffunction[locB[0]][locB[1]].calculate(selffunction,xval)
        else:
            self.inputB = xval
    
##    def replaceX(self,val):
##        if self.inputA=='x':
##            self.inputA = val
##        elif self.inputB=='x':
##            self.inputB = val
