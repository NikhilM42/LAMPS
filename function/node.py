import math
from random import random

TRANSFORM_COUNT = 6
COMBINER_COUNT = 4

TRANSFORMER_OPS = {
    "NOTHING": 0,
    "SIN": 1,
    "COS": 2,
    "SQRT": 3,
    "ABS": 4,
    "EXP": 5,
    "TAN": 6,
    "LOG_E": 7,
    "LOG_10": 8,
    "ASIN": 9,
    "ACOS": 10,
    "ATAN": 11,
}

COMBINER_OPS = {
    "ADD": 0,
    "SUBTRACT": 1,
    "MULTIPLY": 2,
    "POWER": 3,
    "DIVIDE": 4,
    "MODULO": 5,
    "LOG_WITH_BASE": 6,
}

OPERATION_TYPES = {
    "TRANSFORMER": 1,
    "COMBINER": 2,
}

NODE_TYPES = {
    "RANDOM": 0,
    "RANDOM_ROOT": 1,
    "CUSTOM": 2,
}


class node:
    operation_type = 1
    operation = 1
    inputA = 0
    variable_is_A = 0
    inputB = 0
    variable_is_B = 0
    outputY = 0

    def __init__(self, node_type=NODE_TYPES["RANDOM"], opType=0, op=0, varA=0, varB=0):
        if node_type == NODE_TYPES["RANDOM"]:
            self.build_random_node()
        elif node_type == NODE_TYPES["RANDOM_ROOT"]:
            self.build_random_root_node()
        elif node_type == NODE_TYPES["CUSTOM"]:
            self.build_custom_node(opType, op, varA, varB)
        else:
            raise ValueError("Invalid node type")

    def build_custom_node(self, opType: OPERATION_TYPES, op: int, varA, varB):
        # guard against bad values for opType
        if opType < OPERATION_TYPES["TRANSFORMER"] or opType > OPERATION_TYPES["COMBINER"]:
            return

        # guard against bad values for op
        if (opType == OPERATION_TYPES["TRANSFORMER"] and (op < 0 or op >= TRANSFORM_COUNT)) or (opType == OPERATION_TYPES["COMBINER"] and (op < 0 or op >= COMBINER_COUNT)):
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

        self.inputA = 'x'
        if self.inputA == 'x':
            self.variable_is_A = 1
        else:
            self.variable_is_A = 0

        if self.operation_type == OPERATION_TYPES["TRANSFORMER"]:
            self.operation = int(random()*1000) % TRANSFORM_COUNT
        else:
            self.operation = int(random()*1000) % COMBINER_COUNT
            self.inputB = self.randomly_create_value_or_variable()

            if self.inputB == 'x':
                self.variable_is_B = 1
            else:
                self.variable_is_B = 0

    def build_random_root_node(self):
        print("Not implemented yet")

    def randomly_create_value_or_variable(self):
        randVar = int(random()*1000) % 3

        if randVar == 0:
            return 'x'
        else:
            return int(random()*10) + 1

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
        if self.operation_type == OPERATION_TYPES["TRANSFORMER"]:
            self.outputY = node._transform(self.operation, variable_a)
        else:
            self.outputY = node._combine(
                self.operation, variable_a, variable_b)

        return self.outputY

    def _transform(function_index: int, input_value: float | int) -> float:
        if function_index == TRANSFORMER_OPS["NOTHING"]:
            return input_value
        elif function_index == TRANSFORMER_OPS["SIN"]:
            return math.sin(input_value)
        elif function_index == TRANSFORMER_OPS["COS"]:
            return math.cos(input_value)
        elif function_index == TRANSFORMER_OPS["TAN"]:
            return math.tan(input_value)
        elif function_index == TRANSFORMER_OPS["SQRT"]:
            return math.sqrt(input_value)
        elif function_index == TRANSFORMER_OPS["ABS"]:
            return abs(input_value)
        elif function_index == TRANSFORMER_OPS["EXP"]:
            return math.exp(input_value)
        elif function_index == TRANSFORMER_OPS["LOG_E"]:
            if input_value == 0:
                input_value += 0.1
            return math.log(abs(input_value))
        elif function_index == TRANSFORMER_OPS["LOG_10"]:
            if input_value == 0:
                input_value += 0.1
            return math.log10(math.abs(input_value))
        elif function_index == TRANSFORMER_OPS["ASIN"]:
            # if input_value > 1 or input_value < -1:
            #     raise ValueError(input_value)
            return math.asin(input_value % 2 - 1)
        elif function_index == TRANSFORMER_OPS["ACOS"]:
            # if input_value > 1 or input_value < -1:
            #     raise ValueError(input_value)
            return math.acos(input_value % 2 - 1)
        elif function_index == TRANSFORMER_OPS["ATAN"]:
            return math.atan(input_value)
        else:
            raise ValueError(function_index)

    def _combine(function_index: int, input_value_a: float | int, input_value_b: float | int) -> float:
        if function_index == COMBINER_OPS["ADD"]:
            return input_value_a + input_value_b
        elif function_index == COMBINER_OPS["SUBTRACT"]:
            return input_value_a - input_value_b
        elif function_index == COMBINER_OPS["MULTIPLY"]:
            return input_value_a * input_value_b
        elif function_index == COMBINER_OPS["DIVIDE"]:
            if input_value_b == 0:
                raise ValueError("Cannot divide by zero")
            return input_value_a / input_value_b
        elif function_index == COMBINER_OPS["POWER"]:
            return input_value_a ** input_value_b
        elif function_index == COMBINER_OPS["MODULO"]:
            if input_value_b == 0:
                raise ValueError("Cannot modulo by zero")
            return input_value_a % input_value_b
        elif function_index == COMBINER_OPS["LOG"]:
            if input_value_a == 0:
                raise ValueError("Cannot log with a base zero")
            return math.log(abs(input_value_a), input_value_b)
        else:
            raise ValueError(function_index)

    # prints the transformation equation
    def print_transform(self):
        if self.operation == TRANSFORMER_OPS["NOTHING"]:
            print("No change: ", self.inputA, sep=' ', end=' ')
        elif self.operation == TRANSFORMER_OPS["SIN"]:
            print("sin(", self.inputA, ")", sep=' ', end=' ')
        elif self.operation == TRANSFORMER_OPS["COS"]:
            print("cos(", self.inputA, ")", sep=' ', end=' ')
        elif self.operation == TRANSFORMER_OPS["SQRT"]:
            print("sqrt(", self.inputA, ")", sep=' ', end=' ')
        elif self.operation == TRANSFORMER_OPS["ABS"]:
            print("abs(", self.inputA, ")", sep=' ', end=' ')
        elif self.operation == TRANSFORMER_OPS["EXP"]:
            print("exp(", self.inputA, ")", sep=' ', end=' ')
        else:
            print("unknown transformation function")

    # prints the combiner equation
    def print_combine(self):
        if self.operation == COMBINER_OPS["ADD"]:
            print(self.inputA, "+", self.inputB, sep=' ', end=' ')
        elif self.operation == COMBINER_OPS["SUBTRACT"]:
            print(self.inputA, "-", self.inputB, sep=' ', end=' ')
        elif self.operation == COMBINER_OPS["MULTIPLY"]:
            print(self.inputA, "*", self.inputB, sep=' ', end=' ')
        elif self.operation == COMBINER_OPS["DIVIDE"]:
            print(self.inputA, "/", self.inputB, sep=' ', end=' ')
        elif self.operation == COMBINER_OPS["POWER"]:
            print(self.inputA, "^", self.inputB, sep=' ', end=' ')
        else:
            print("unknown combiner function")

    # prints the nodes equation
    def print_node(self):
        if self.operation_type == 1:
            self.print_transform()
        else:
            self.print_combine()
