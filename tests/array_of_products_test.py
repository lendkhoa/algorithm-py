import unittest
import sys
sys.path.append('../algorithm_py')
from array_of_products import arrayOfProducts

class TestArrayOfProducts(unittest.TestCase):
    def test_example_case(self):
        input_array = [1, 2, 3, 4]
        expected_output = [24, 12, 8, 6]
        self.assertEqual(arrayOfProducts(input_array), expected_output)


if __name__ == '__main__':
    unittest.main()
