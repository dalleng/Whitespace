import unittest
from whitespace import whitespace


class StackManipulationTest(unittest.TestCase):

    def test_output_positive_numbers(self):
        output1 = '   \t\n\t\n \t\n\n\n'
        output2 = '   \t \n\t\n \t\n\n\n'
        output3 = '   \t\t\n\t\n \t\n\n\n'
        output0 = '    \n\t\n \t\n\n\n'
        self.assertEqual(whitespace(output1), '1')
        self.assertEqual(whitespace(output2), '2')
        self.assertEqual(whitespace(output3), '3')
        self.assertEqual(whitespace(output0), '0')

    def test_output_negative__numbers(self):
        output_negative_1 = '  \t\t\n\t\n \t\n\n\n'
        output_negative_2 = '  \t\t \n\t\n \t\n\n\n'
        output_negative_3 = '  \t\t\t\n\t\n \t\n\n\n'
        self.assertEqual(whitespace(output_negative_1), '-1')
        self.assertEqual(whitespace(output_negative_2), '-2')
        self.assertEqual(whitespace(output_negative_3), '-3')

    def test_output_letters(self):
        output_a = '   \t     \t\n\t\n  \n\n\n'
        output_b = '   \t    \t \n\t\n  \n\n\n'
        output_c = '   \t    \t\t\n\t\n  \n\n\n'
        self.assertEqual(whitespace(output_a), 'A')
        self.assertEqual(whitespace(output_b), 'B')
        self.assertEqual(whitespace(output_c), 'C')

    def test_swap(self):
        push_A = '   \t     \t\n'
        push_B = '   \t    \t \n'
        swap = ' \n\t'
        print_output = '\t\n  '
        exit = '\n\n\n'
        self.assertEqual(whitespace('{}{}{}{}{}{}'.format(
            push_A, push_B, swap, print_output, print_output, exit)), 'AB')

    def test_duplicate(self):
        push_A = '   \t     \t\n'
        dup_A = ' \n '
        print_output = '\t\n  '
        exit = '\n\n\n'
        self.assertEqual(whitespace('{}{}{}{}{}'.format(
            push_A, dup_A, print_output, print_output, exit)), 'AA')

    def test_discard(self):
        push_A = '   \t     \t\n'
        push_B = '   \t    \t \n'
        discard = ' \n\n'
        print_output = '\t\n  '
        exit = '\n\n\n'
        self.assertEqual(whitespace('{}{}{}{}{}'.format(
            push_A, push_B, discard, print_output, exit)), 'A')


class ArithmethicTest(unittest.TestCase):

    def test_addition(self):
        push1 = '   \t\n'
        push2 = '   \t \n'
        add = '\t   '
        print_output = '\t\n \t'
        exit = '\n\n\n'

        # 1 + 2
        self.assertEqual(whitespace('{}{}{}{}{}'.format(
            push1, push2, add, print_output, exit)), '3')

        push_negative_1 = '  \t\t\n'

        # 1 + (-1)
        self.assertEqual(whitespace('{}{}{}{}{}'.format(
            push1, push_negative_1, add, print_output, exit)), '0')

    def test_subtraction(self):
        push1 = '   \t\n'
        push2 = '   \t \n'
        sub = '\t  \t'
        print_output = '\t\n \t'
        exit = '\n\n\n'

        # 1 - 2
        self.assertEqual(whitespace('{}{}{}{}{}'.format(
            push1, push2, sub, print_output, exit)), '-1')

        # 2 - 1
        self.assertEqual(whitespace('{}{}{}{}{}'.format(
            push2, push1, sub, print_output, exit)), '1')

    def test_multiplication(self):
        push2 = '   \t \n'
        mult = '\t  \n'
        print_output = '\t\n \t'
        exit = '\n\n\n'

        # 2 * 2
        self.assertEqual(whitespace('{}{}{}{}{}'.format(
            push2, push2, mult, print_output, exit)), '4')

        push0 = '   \n'

        # 2 * 0
        self.assertEqual(whitespace('{}{}{}{}{}'.format(
            push0, push2, mult, print_output, exit)), '0')

    def test_division(self):
        push2 = '   \t \n'
        push4 = '   \t  \n'
        div = '\t \t '
        print_output = '\t\n \t'
        exit = '\n\n\n'

        # 4 / 2
        self.assertEqual(whitespace('{}{}{}{}{}'.format(
            push4, push2, div, print_output, exit)), '2')

        push0 = '   \n'

        # 0 / 2
        self.assertEqual(whitespace('{}{}{}{}{}'.format(
            push0, push2, div, print_output, exit)), '0')

        # 2 / 0
        with self.assertRaises(ZeroDivisionError):
            whitespace('{}{}{}{}{}'.format(
                push2, push0, div, print_output, exit))


if __name__ == '__main__':
    unittest.main()
