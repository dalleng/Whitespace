import unittest
from whitespace import whitespace


class StackManipulationTest(unittest.TestCase):

    def test_output_positive_numbers(self):
        output1 = "   \t\n\t\n \t\n\n\n"
        output2 = "   \t \n\t\n \t\n\n\n"
        output3 = "   \t\t\n\t\n \t\n\n\n"
        output0 = "    \n\t\n \t\n\n\n"
        self.assertEquals(whitespace(output1), "1")
        self.assertEquals(whitespace(output2), "2")
        self.assertEquals(whitespace(output3), "3")
        self.assertEquals(whitespace(output0), "0")

    def test_output_negative_numbers(self):
        outputNegative1 = "  \t\t\n\t\n \t\n\n\n"
        outputNegative2 = "  \t\t \n\t\n \t\n\n\n"
        outputNegative3 = "  \t\t\t\n\t\n \t\n\n\n"
        self.assertEquals(whitespace(outputNegative1), "-1")
        self.assertEquals(whitespace(outputNegative2), "-2")
        self.assertEquals(whitespace(outputNegative3), "-3")

    def test_output_letters(self):
        outputA = "   \t     \t\n\t\n  \n\n\n"
        outputB = "   \t    \t \n\t\n  \n\n\n"
        outputC = "   \t    \t\t\n\t\n  \n\n\n"
        self.assertEquals(whitespace(outputA), "A")
        self.assertEquals(whitespace(outputB), "B")
        self.assertEquals(whitespace(outputC), "C")


if __name__ == '__main__':
    unittest.main()
