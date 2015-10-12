import unittest
from whitespace import whitespace


class StackManipulationTest(unittest.TestCase):

    def test_output_positive_numbers(self):
        push_pop_print1 = '   \t\n\t\n \t\n\n\n'
        push_pop_print2 = '   \t \n\t\n \t\n\n\n'
        push_pop_print3 = '   \t\t\n\t\n \t\n\n\n'
        push_pop_print0 = '    \n\t\n \t\n\n\n'
        self.assertEqual(whitespace(push_pop_print1), '1')
        self.assertEqual(whitespace(push_pop_print2), '2')
        self.assertEqual(whitespace(push_pop_print3), '3')
        self.assertEqual(whitespace(push_pop_print0), '0')

    def test_output_negative__numbers(self):
        push_pop_print_negative_1 = '  \t\t\n\t\n \t\n\n\n'
        push_pop_print_negative_2 = '  \t\t \n\t\n \t\n\n\n'
        push_pop_print_negative_3 = '  \t\t\t\n\t\n \t\n\n\n'
        self.assertEqual(whitespace(push_pop_print_negative_1), '-1')
        self.assertEqual(whitespace(push_pop_print_negative_2), '-2')
        self.assertEqual(whitespace(push_pop_print_negative_3), '-3')

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

    def test_discard_top(self):
        push_A = '   \t     \t\n'
        push_B = '   \t    \t \n'
        discard_top = ' \n\n'
        print_output = '\t\n  '
        exit = '\n\n\n'
        self.assertEqual(whitespace('{}{}{}{}{}'.format(
            push_A, push_B, discard_top, print_output, exit)), 'A')

    def test_duplicate_nth(self):
        push1 = '   \t\n'
        push2 = '   \t \n'
        push3 = '   \t\t\n'
        duplicate3 = '\t\n \t'
        exit = '\n\n\n'

        self.assertEqual(whitespace('{}{}{}{}{}'.format(
            push1, push2, push3, duplicate3, exit)), '3')

        code = (
            # push 0
            '  \t\n'
            # push 2
            '   \t \n'
            # push 3
            '   \t\t\n'
            # duplicate the -1th value from the top
            ' \t \t\t\n'
            # pop and print as number
            '\t\n \t'
            '\n\n\n'
        )

        with self.assertRaises(IndexError):
            whitespace(code)

    def test_discard_top_n(self):
        code = (
            # push -1
            '  \t\t\n'
            # push 2
            '   \t \n'
            # push 1
            '   \t\n'
            # push 3
            '   \t\t\n'
            # push 6
            '   \t\t \n'
            # push 5
            '   \t \t\n'
            # push 7
            '   \t\t\t\n'
            # swap first two
            ' \n\t'
            # discard top 3 below top
            ' \t\n \t\t\n'
            # pop and print as number
            '\t\n \t'
            '\t\n \t'
            '\t\n \t'
            '\t\n \t'
            '\n\n\n'
        )

        self.assertEqual(whitespace(code), '512-1')


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

    def test_modulo(self):
        push3 = '   \t\t\n'
        push4 = '   \t  \n'
        mod = '\t \t\t'
        print_output = '\t\n \t'
        exit = '\n\n\n'

        # 4 % 3
        self.assertEqual(whitespace('{}{}{}{}{}'.format(
            push4, push3, mod, print_output, exit)), '1')

        push0 = '   \n'

        # 0 % 3
        self.assertEqual(whitespace('{}{}{}{}{}'.format(
            push0, push3, mod, print_output, exit)), '0')

        # 3 % 0
        with self.assertRaises(ZeroDivisionError):
            whitespace('{}{}{}{}{}'.format(
                push3, push0, mod, print_output, exit))


class HeapTest(unittest.TestCase):

    def test_store_retrieve(self):
        push3 = '   \t\t\n'
        push4 = '   \t  \n'
        heap_store = '\t\t '
        heap_retrieve = '\t\t\t'
        print_output = '\t\n \t'
        exit = '\n\n\n'
        self.assertEqual(whitespace('{}{}{}{}{}{}{}'.format(
            push3, push4, heap_store, push3,
            heap_retrieve, print_output, exit)), '4')


class InputTest(unittest.TestCase):

    def test_read_char(self):
        inp = 'A'
        push1 = '   \t\n'
        read_char = '\t\n\t '
        heap_retrieve = '\t\t\t'
        print_output = '\t\n  '
        exit = '\n\n\n'
        self.assertEqual(whitespace('{}{}{}{}{}{}'.format(
            push1, read_char, push1, heap_retrieve,
            print_output, exit), inp=inp), 'A')

    def test_read_number(self):
        inp = '12345\n'
        push1 = '   \t\n'
        read_number = '\t\n\t\t'
        heap_retrieve = '\t\t\t'
        print_output = '\t\n \t'
        exit = '\n\n\n'

        self.assertEqual(whitespace('{}{}{}{}{}{}'.format(
            push1, read_number, push1, heap_retrieve,
            print_output, exit), inp=inp), '12345')

        inp = '2A\n'

        self.assertEqual(whitespace('{}{}{}{}{}{}'.format(
            push1, read_number, push1, heap_retrieve,
            print_output, exit), inp=inp), '42')


if __name__ == '__main__':
    unittest.main()
