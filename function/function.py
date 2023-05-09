#!/usr/bin/env python3
from random import random

from .node import NODE_TYPES, OPERATION_TYPES, COMBINER_OPS, node

# This is a class that represents a function.


class function:
    number_of_events = 0
    equation: list[list[node]] = []
    result: list[int] = []

    def __init__(self, max_events=10, event_count=0):
        if (event_count < 1):
            self.number_of_events = int(3 + (random() * (max_events - 3)))
        else:
            self.number_of_events = event_count

        self.equation = []

        # Create a random row of nodes.
        # Each node represents a term of the function.
        # Each node will have an x value.
        for event_index in range(self.number_of_events):
            self.equation.append(
                [node(NODE_TYPES["CUSTOM"], OPERATION_TYPES["COMBINER"], COMBINER_OPS["MULTIPLY"], 'x', 1)])
            # self.equation[event_index][0].print_node()
            # Create a random number of operations to apply to the node.
            number_of_operations = int(random()*1000) % 5+1
            for operation in range(number_of_operations):
                self.equation[event_index].append(node())
                # self.equation[event_index][operation + 1].print_node()
            # print()
    
    # reset result.
    def reset_result(self):
        self.result = []

    # calculates the answer using the given xval.
    def calculate(function, max_x_val: int, index: int):
        result = []
        for data_point_index in range(max_x_val):
            answer = 0
            new_x_val = data_point_index
            # print('Input:' + str(x_val))
            for i in range(function.number_of_events):
                for j in range(len(function.equation[i])):
                    new_x_val = function.equation[i][j].calculate(new_x_val)

                answer += new_x_val
            # print("Processing ", str(data_point_index + 1), " out of " + str(max_x_val))
            # print('Output:'+ str(answer))
            result.append(answer)
        # function.result = result
        # print('Done calculating function.')
        return (index, result)

    # print the function.
    def print_function(self):
        for i in range(self.number_of_events):
            for j in range(len(self.equation[i])):
                self.equation[i][j].print_node()
            print()

    # mutatefunction mutates a random part of the function.
    def mutate_function(self):
        # generate a random number between 0 and the number of events - 1.
        num_of_events_to_replace = int(random()*(self.number_of_events - 1))
        for i in range(num_of_events_to_replace):
            # generate a random index number greater than 0 and less than the number of events. 
            index = int(random()*(self.number_of_events - 1) + 1)
            # replace the event at the index with a new set of nodes.
            number_of_operations = int(random()*1000) % 10+1
            for operation in range(number_of_operations):
                self.equation[index].append(node())
        

    def merge_functions(self, other):
        print('To be implemented')
