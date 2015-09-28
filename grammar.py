from commands import push_stack, pop_print, pop_print_chr

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
