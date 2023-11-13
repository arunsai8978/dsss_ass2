from math_quiz import random_number, random_operator, math_operation
import unittest
import random


class TestMathGame(unittest.TestCase):

    def test_function_A(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 100
        for _ in range(1000):  # Test a large number of random values
            rand_num = random_number(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_function_B(self):
        random.seed(42)
        # Call the function multiple times and check if the result is one of the expected operators
        for _ in range(100):  # You can adjust the number of iterations based on your preference
            result = random_operator()
            self.assertIn(result, ['+', '-', '*'])

    def test_function_C(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (7, 3, '-', '7 - 3', 4),
                (4, 6, '*', '4 * 6', 24)
            ]
            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                result_problem, result_answer = math_operation(num1, num2, operator)

                # Check if the problem and answer match the expected values
                self.assertEqual(result_problem, expected_problem)
                self.assertEqual(result_answer, expected_answer)

if __name__ == "__main__":
    unittest.main()
