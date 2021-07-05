import math
from random import random
from .nodes import node

class function:
    numberofevents = 0
    equation = []

    def __init__(self,eventcount=0):
        if(eventcount < 1):
            self.numberofevents = int(3 + (random() * (10 - 3)))
        else:
            self.numberofevents = eventcount
        
        self.equation = []
        equationvariablerow = []

        for event in range(self.numberofevents):
            equationvariablerow.append(node(2,3,1,'x'))
        
        self.equation.append(equationvariablerow)
        numberofoperations = int(random()*1000)%10+1
        
        for operation in range(numberofoperations):
            nodecount = int(random()*1000)%10+1
            noderow = []
            for n in range(nodecount):
                noderow.append(node(layer,len(layer[randrow])))
                
            function.append(noderow)

    def calculatefunction(function, xval):
        
        return function

    def mutatefunction(function):
        return function
        
    def mergefunctions(functionA,functionB):
        return function

    def functionwriter(function):
        return function