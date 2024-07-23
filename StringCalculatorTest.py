import unittest
from StringCalculator import StringCalculator

class TestStringCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = StringCalculator()

    def test_empty_string(self):
        self.assertEqual(self.calc.add(""), 0)

    def test_single_number(self):
        self.assertEqual(self.calc.add("1"), 1)
        self.assertEqual(self.calc.add("5"), 5)

    def test_two_numbers(self):
        self.assertEqual(self.calc.add("1,2"), 3)
        self.assertEqual(self.calc.add("3,4"), 7)

    def test_multiple_numbers(self):
        self.assertEqual(self.calc.add("1,2,3"), 6)
        self.assertEqual(self.calc.add("4,5,6,7"), 22)

    def test_new_lines_between_numbers(self):
        self.assertEqual(self.calc.add("1\n2,3"), 6)
        self.assertEqual(self.calc.add("4\n5\n6"), 15)

    def test_different_delimiters(self):
        self.assertEqual(self.calc.add("//;\n1;2"), 3)
        self.assertEqual(self.calc.add("//|\n1|2|3"), 6)
        self.assertEqual(self.calc.add("//[***]\n1***2***3"), 6)

    def test_negative_numbers(self):
        with self.assertRaises(ValueError) as cm:
            self.calc.add("1,-2,3")
        self.assertEqual(str(cm.exception), "Negatives not allowed: -2")
        with self.assertRaises(ValueError) as cm:
            self.calc.add("//;\n1;-2;3;-4")
        self.assertEqual(str(cm.exception), "Negatives not allowed: -2, -4")

    def test_ignore_numbers_bigger_than_1000(self):
        self.assertEqual(self.calc.add("2,1001"), 2)
        self.assertEqual(self.calc.add("1000,1001,2"), 1002)

    def test_multiple_delimiters_of_any_length(self):
        self.assertEqual(self.calc.add("//[***]\n1***2***3"), 6)
        self.assertEqual(self.calc.add("//[%%]\n4%%5%%6"), 15)
        self.assertEqual(self.calc.add("//[***][%%%]\n1***2%%%3"), 6)

if __name__ == "__main__":
    unittest.main()
