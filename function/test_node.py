import unittest
from .node import node
from .node import COMBINER_COUNT

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
        


if __name__ == '__main__':
    unittest.main()