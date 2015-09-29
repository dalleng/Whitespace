from commands import (
    push_stack,
    duplicate_top,
    swap_first_two,
    discard_top,
    addition,
    subtraction,
    multiplication,
    division,
    pop_print,
    pop_print_chr,
    exit_program
)

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

"""
IMP [space] - Stack Manipulation

    [space] (number): Push n onto the stack.

    [tab][space] (number): Duplicate the nth value from the top of the stack.

    [tab][line-feed] (number): Discard the top n values below the top of the
    stack from the stack. (For n<0 or n>=stack.length, remove everything but
    the top value.)

    [line-feed][space]: Duplicate the top value on the stack.

    [line-feed][tab]: Swap the top two value on the stack.

    [line-feed][line-feed]: Discard the top value on the stack.

"""
PUSH_STACK = r'{SPACE}{NUMBER}'.format(NUMBER=NUMBER, **chars)
DUPLICATE_TOP = r'{LINE_FEED}{SPACE}'.format(**chars)
SWAP_FIRST_TWO = r'{LINE_FEED}{TAB}'.format(**chars)
DISCARD_TOP = r'{LINE_FEED}{LINE_FEED}'.format(**chars)

"""
IMP [tab][space] - Arithmetic

    [space][space]: Pop a and b, then push b+a.

    [space][tab]: Pop a and b, then push b-a.

    [space][line-feed]: Pop a and b, then push b*a.

    [tab][space]: Pop a and b, then push b/a*. If a is zero, throw an error.
    *Note that the result is defined as the floor of the quotient.

    [tab][tab]: Pop a and b, then push b%a*. If a is zero, throw an error.
    *Note that the result is defined as the remainder after division and sign
    (+/-) of the divisor (a).
"""
ADDITION = r'{SPACE}{SPACE}'.format(**chars)
SUBTRACTION = r'{SPACE}{TAB}'.format(**chars)
MULTIPLICATION = r'{SPACE}{LINE_FEED}'.format(**chars)
DIVISION = r'{TAB}{SPACE}'.format(**chars)

POP_PRINT = r'{SPACE}{TAB}'.format(**chars)
POP_PRINT_CHR = r'{SPACE}{SPACE}'.format(**chars)
EXIT = r'{LINE_FEED}{LINE_FEED}'.format(**chars)

grammar = {
    STACK_MANIPULATION: {
        PUSH_STACK: push_stack,
        DUPLICATE_TOP: duplicate_top,
        SWAP_FIRST_TWO: swap_first_two,
        DISCARD_TOP: discard_top,
    },
    ARITHMETIC: {
        ADDITION: addition,
        SUBTRACTION: subtraction,
        MULTIPLICATION: multiplication,
        DIVISION: division,
    },
    IO: {
        POP_PRINT: pop_print,
        POP_PRINT_CHR: pop_print_chr
    },
    FLOW_CONTROL: {
        EXIT: exit_program
    }
}
