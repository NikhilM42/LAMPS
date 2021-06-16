from .nodes import node

class function:

    ##function dictionary
    transformer = {
        '1': lambda a: sin(a),
        '2': lambda a: cos(a),
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

    functionTypes = {
        '1': transformer,
        '2': combiner
        }

    def generatefunction():
        eventcount = int(3 + (random() * (10 - 3)))
        function = []
        start = []

        for event in range(eventcount):
            start.append(node(2,3,1,'x'))

        function.append(start)
        layercount = int(random()*1000)%10+1

        for layer in range(layercount):
            nodecount = int(random()*1000)%10+1
            noderow = []
            for n in range(nodecount):
                functiontype = int(random()*1000)%2+1
                
                if functiontype==1:
                    formula = int(random()*1000)%6+1
                    randrow = int(random()*1000)%layer
                    randcol = int(random()*1000)%len(layer[randrow])
                    num = [randrow,randcol]
                    noderow.append(node(functiontype,formula,num))
                else:
                    formula = int(random()*1000)%7+1
                    randrow = int(random()*1000)%layer
                    randcol = int(random()*1000)%len(layer[randrow])
                    numone = [randrow,randcol]
                    randrow = int(random()*1000)%layer
                    randcol = int(random()*1000)%len(layer[randrow])
                    numtwo = [randrow,randcol]
                    noderow.append(node(functiontype,formula,numone,numtwo))
            function.append(noderow)
        
        return function

    def calculatefunction(function, xval):
        return function

    def mutatefunction(function):
        
    def mergefunctions(functionA,functionB):

    def functionwriter(function):