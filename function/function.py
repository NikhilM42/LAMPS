#!/usr/bin/env python3
from random import random

from .node import COMBINER, COMBINER_OPS, node

# This is a class that represents a function.
class function:
    number_of_events = 0
    equation: list[list[node]] = []

    def __init__(self, event_count=0):
        if (event_count < 1):
            self.number_of_events = int(3 + (random() * (10 - 3)))
        else:
            self.number_of_events = event_count

        self.equation = []

        # Create a random row of nodes.
        # Each node represents a term of the function.
        # Each node will have an x value.
        for event_index in range(self.number_of_events):
            self.equation.append([node(COMBINER, COMBINER_OPS["MULTIPLY"], 'x', 1)])
            # self.equation[event_index][0].print_node()
            # Create a random number of operations to apply to the node.
            number_of_operations = int(random()*1000) % 10+1
            for operation in range(number_of_operations):
                self.equation[event_index].append(node())
                # self.equation[event_index][operation + 1].print_node()
            # print()

    # calculates the answer using the given xval.
    def calculate_function(self, x_val: int):
        answer = 0
        new_x_val = x_val
        # print('Input:' + str(x_val))
        for i in range(self.number_of_events):
            for j in range(len(self.equation[i])):
                # try:
                new_x_val = self.equation[i][j].calculate(new_x_val)
                # except ValueError:
                #     raise Exception('Error in function calculation due to value.')
                # except:
                #     raise Exception('Error in function calculation.')
                
            answer += new_x_val
        # print('Output:'+ str(answer))
        # self.print_function()
        return answer

    # print the function.
    def print_function(self):
        for i in range(self.number_of_events):
            for j in range(len(self.equation[i])):
                self.equation[i][j].print_node()

    # mutatefunction mutates a random part of the function.
    def mutate_function(function):
        return function

    def merge_functions(functionA, functionB):
        return function

    def function_writer(function):
        return function
