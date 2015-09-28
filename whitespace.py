from __future__ import print_function

import re
import sys
import unittest

import pdb


"""
Whitespace is an esoteric programming language that uses only three characters:

    [space] or " " (ASCII 32)
    [tab] or "\t" (ASCII 9)
    [line-feed] or "\n" (ASCII 10)

"""
chars = {'SPACE': r' ', 'TAB': r'\t', 'LINE_FEED': r'\n'}


""" Each command in whitespace begins with an Instruction Modification
    Parameter (IMP).
"""
STACK_MANIPULATION = r'{SPACE}'.format(**chars)
ARITHMETIC = r'{TAB}{SPACE}'.format(**chars)
HEAP_ACCESS = r'{TAB}{TAB}'.format(**chars)
IO = r'{TAB}{LINE_FEED}'.format(**chars)
FLOW_CONTROL = r'{LINE_FEED}'.format(**chars)


"""
Parsing Numbers

    Numbers begin with a [sign] symbol. [tab] -> negative,
    or [space] -> positive.

    Numbers end with a [terminal] symbol: [line-feed].

    Between the sign symbol and the terminal symbol are binary digits
    [space] -> binary-0, or [tab] -> binary-1.

    A number expression [sign][terminal] will be treated as zero.
"""
SIGN = r'(?P<sign>{TAB}|{SPACE})'.format(**chars)
DIGIT = r'(?P<digit>({SPACE}|{TAB})*)'.format(**chars)
NUMBER = r'{SIGN}{DIGIT}{LINE_FEED}'.format(SIGN=SIGN, DIGIT=DIGIT, **chars)

PUSH_STACK = r'{SPACE}{NUMBER}'.format(NUMBER=NUMBER, **chars)
POP_PRINT = r'{SPACE}{TAB}'.format(**chars)
POP_PRINT_CHR = r'{SPACE}{SPACE}'.format(**chars)
EXIT = r'{LINE_FEED}{LINE_FEED}'.format(**chars)


def push_stack(inp, output, stack, heap, sign=None, digit=None, **kwargs):
    assert digit is not None
    assert sign is not None

    digit = digit.replace(' ', '0').replace('\t', '1')
    sign = sign.replace(' ', '1').replace('\t', '-1')
    digit = int(sign) * int(digit, base=2)
    stack.append(digit)

    return inp, output


def pop_print(inp, output, stack, heap, **kwargs):
    output += str(stack.pop())
    return inp, output


def pop_print_chr(inp, output, stack, heap, **kwargs):
    output += chr(int(stack.pop()))
    return inp, output


def exit(inp, output, stack, heap, **kwargs):
    raise StopProgram


grammar = {
    STACK_MANIPULATION: {
        PUSH_STACK: push_stack
    },
    IO: {
        POP_PRINT: pop_print,
        POP_PRINT_CHR: pop_print_chr
    },
    FLOW_CONTROL: {
        EXIT: exit
    }
}


def whitespace(code, inp=''):
    output = ''
    stack = []
    heap = {}
    program = []

    try:
        while code:
            code, func, kwargs = parse(code)
            program.append((func, kwargs))
            # print(kwargs)
    except ParseError as e:
        print('Parse Error: {}'.format(e.code), file=sys.stderr)
        sys.exit(1)

    for func, kwargs in program:
        try:
            i, o = func(inp, output, stack, heap, **kwargs)
            inp = i
            output = o
        except StopProgram:
            return output

    raise RuntimeError('Unclean termination')


class StopProgram(Exception):
    def __init__(self):
        pass


class ParseError(Exception):
    def __init__(self, code):
        self.code = repr(code)

    def __str__(self):
        return repr(self.code)


def parse(code):
    for imp in grammar:
        imp_match = re.match(imp, code)

        if imp_match:
            imp_matched = imp_match.group(0)

            for command, func in grammar[imp].items():
                command_match = re.match(command, code[len(imp_matched):])

                if command_match:
                    command_matched = command_match.group(0)
                    code = code[len(imp_matched) + len(command_matched):]
                    return code, func, command_match.groupdict()

    raise ParseError(code)


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
