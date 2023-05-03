import unittest
from node import node, COMBINER_COUNT, TRANSFORMER_OPS, COMBINER_OPS

# unit test for node
class TestNodeMethods(unittest.TestCase):
    def test_build_node(self):
        print("test_build_node")
    
    def test_build_random_node(self):
        print("test_build_random_node")
    
    def test_randomly_create_value_or_variable(self):
        print("test_randomly_create_value_or_variable")
    
    def test_set_operation_type(self):
        print("test_set_operation_type")
    
    def test_calculate(self):
        print("test_calculate")
    
    def test_transform(self):
        print("test_transform")

    # test the _combine method for the node class
    def test_combine(self):
        print("test_combine")
        # a negative function_index value should raise a ValueError
        with self.assertRaises(ValueError):
            result = node._combine(-1,1,1)
        # a function_index value greater than the number of functions should raise a ValueError
        with self.assertRaises(ValueError):
            result = node._combine(COMBINER_COUNT,1,1)
        # a function_index value of 0 will add input_value_a with input_value_b
        result = node._combine(COMBINER_OPS['ADD'], 1, 1)
        self.assertEqual(result, 2)
        # a function_index value of 1 will subtract input_value_b from input_value_a
        result = node._combine(COMBINER_OPS['SUBTRACT'], 2, 1)
        self.assertEqual(result, 1)
        # a function_index value of 2 will multiply input_value_a with input_value_b
        result = node._combine(COMBINER_OPS['MULTIPLY'], 2, 2)
        self.assertEqual(result, 4)
        # a function_index value of 3 will divide input_value_a by input_value_b
        result = node._combine(COMBINER_OPS['DIVIDE'], 4, 2)
        self.assertEqual(result, 2)

if __name__ == '__main__':
    unittest.main()