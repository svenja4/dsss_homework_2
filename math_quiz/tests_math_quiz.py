import unittest
from math_quiz import createRandomInteger, randomArithmeticOperator, calculate


class TestMathGame(unittest.TestCase):

    def test_createRandomInteger(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = createRandomInteger(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_randomArithmeticOperator(self):
        for _ in range(1000):
             operator = randomArithmeticOperator()
             self.assertIn(operator, '+ - *')

    def test_calculate(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7), (8, 3, '+', '8 + 3', 11), (1, 4, '+', '1 + 4', 5), 
                (5, 2, '-', '5 - 2', 3), (7, 1, '-', '7 - 1', 6), (2, 4, '-', '2 - 4', -2), 
                (5, 2, '*', '5 * 2', 10), (9, 1, '*', '9 * 1', 9), (8, 3, '*', '8 * 3', 24)
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                problem, answer = calculate(num1, num2, operator)
                self.assertEqual(problem, expected_problem)
                self.assertEqual(answer, expected_answer)

if __name__ == "__main__":
    unittest.main()
