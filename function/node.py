import math
from random import random

TRANSFORM_COUNT = 12
COMBINER_COUNT = 8

TRANSFORMER_OPS = {
    "NOTHING": 0,
    "SIN": 1,
    "COS": 2,
    "TAN": 3,
    "ASIN": 4,
    "ACOS": 5,
    "ATAN": 6,
    "SQRT": 7,
    "LOG_E": 8,
    "LOG_10": 9,
    "ABS": 10,
    "EXP": 11,
}

COMBINER_OPS = {
    "ADD": 0,
    "SUBTRACT": 1,
    "MULTIPLY": 2,
    "DIVIDE": 3,
    "POWER": 4,
    "MODULO": 5,
    "LOG_WITH_BASE": 6,
}

class node:
    operation_type = 1
    operation = 1
    inputA = 0
    variable_is_A = 0
    inputB = 0
    variable_is_B = 0
    outputY = 0

    def __init__(self, opType=0, op=0, varA=0, varB=0):
        if opType == 0:
            self.build_random_node()
        else:
            self.build_node(opType, op, varA, varB)

    def build_node(self, opType: int, op: int, varA, varB):
        # guard against bad values for opType
        if opType < 0 or opType > 1:
            return

        # guard against bad values for op
        if (opType == 0 and (op < 0 or op >= TRANSFORM_COUNT)) or (opType == 1 and (op < 0 or op >= COMBINER_COUNT)):
            return

        self.inputA = varA
        self.inputB = varB
        self.operation_type = opType
        self.operation = op

        if varB == 'x':
            self.variable_is_B = 1
        else:
            self.variable_is_B = 0

        if varA == 'x':
            self.variable_is_A = 1
        else:
            self.variable_is_A = 0

    def build_random_node(self):
        self.operation_type = int(random()*1000) % 2

        self.inputA = self.randomlyCreateValueOrVariable()
        if self.inputA == 'x':
            self.variable_is_A = 1
        else:
            self.variable_is_A = 0

        if self.operation_type == 1:
            self.operation = int(random()*1000) % TRANSFORM_COUNT+1
        else:
            self.operation = int(random()*1000) % COMBINER_COUNT+1
            self.inputB = self.randomly_create_value_or_variable()

            if self.inputB == 'x':
                self.variable_is_B = 1
            else:
                self.variable_is_B = 0

    def randomly_create_value_or_variable(self):
        randVar = int(random()*1000) % 3

        if randVar == 0:
            return 'x'
        else:
            return int(random()*1000) + 1

    def set_operation_type(self, opType):
        if opType not in self.operation_types.keys():
            return

        self.operation_type = opType

    def calculate(self, x_val):
        variable_a = self.inputA
        variable_b = self.inputB
        # replace variable_a with xval if variable_is_A == 1
        if self.variable_is_A == 1:
            variable_a = x_val
        # replace variable_b with xval if variable_is_B == 1
        if self.variable_is_B == 1:
            variable_b = x_val

        # check the node's operation type and perform the appropriate calculation and store it
        if self.operation_type == 0:
            self.outputY = node._transform(self.operation, self.outputY)
        else:
            self.outputY = node._combine(
                self.operation, variable_a, variable_b)

        return self.outputY

    def _transform(function_index: int, input_value: float | int) -> float:
        if function_index == 0:
            return input_value
        elif function_index == 1:
            return math.sin(input_value)
        elif function_index == 2:
            return math.cos(input_value)
        elif function_index == 3:
            return math.tan(input_value)
        elif function_index == 4:
            return math.asin(input_value)
        elif function_index == 5:
            return math.acos(input_value)
        elif function_index == 6:
            return math.atan(input_value)
        elif function_index == 7:
            return math.sqrt(input_value)
        elif function_index == 8:
            if input_value == 0:
                input_value += 0.1
            return math.log(math.abs(input_value))
        elif function_index == 9:
            if input_value == 0:
                input_value += 0.1
            return math.log10(math.abs(input_value))
        elif function_index == 10:
            return abs(input_value)
        elif function_index == 11:
            return math.exp(input_value)

    def _combine(function_index: int, input_value_a: float | int, input_value_b: float | int) -> float:
        if function_index == 0:
            return input_value_a + input_value_b
        elif function_index == 1:
            return input_value_a - input_value_b
        elif function_index == 2:
            return input_value_a * input_value_b
        elif function_index == 3:
            return input_value_a / input_value_b
        elif function_index == 4:
            return input_value_a ** input_value_b
        elif function_index == 5:
            return input_value_a % input_value_b
        elif function_index == 6:
            if input_value_a == 0:
                input_value_b += 0.1
            return math.log(math.abs(input_value_a), input_value_b)
        else:
            raise ValueError(function_index)
