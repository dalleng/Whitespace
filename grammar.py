from commands import (
    push_stack,
    duplicate_nth,
    discard_top_n,
    duplicate_top,
    swap_first_two,
    discard_top,
    addition,
    subtraction,
    multiplication,
    division,
    modulo,
    heap_store,
    heap_retrieve,
    read_char,
    read_number,
    pop_print,
    pop_print_chr,
    mark_location,
    jump,
    jump_if_zero,
    jump_if_lt_zero,
    call_subroutine,
    exit_subroutine,
    exit_program
)

"""
Whitespace is an esoteric programming language that uses only three characters:

    [space] or " " (ASCII 32)
    [tab] or "\t" (ASCII 9)
    [line-feed] or "\n" (ASCII 10)

"""
chars = {'SPACE': r' ', 'TAB': r'\t', 'LINE_FEED': r'\n'}
comments = r'[^{SPACE}{TAB}{LINE_FEED}]'.format(**chars)


"""
Each command in whitespace begins with an Instruction Modification
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
Parsing Labels

Labels begin with any number of [tab] and [space] characters.
Labels end with a terminal symbol: [line-feed].
Unlike with numbers, the expression of just [terminal] is valid.
Labels must be unique.
A label may be declared either before or after a command that refers to it.
"""
LABEL = r'(?P<label>({TAB}|{SPACE})*){LINE_FEED}'.format(**chars)


"""
IMP [space] - Stack Manipulation

    [space] (number): Push n onto the stack.

    [tab][space] (number): Copy the nth value from the top of the stack
    and insert the copy on top of the stack.

    [tab][line-feed] (number): Discard the top n values below the top of the
    stack from the stack. (For n<0 or n>=stack.length, remove everything but
    the top value.)

    [line-feed][space]: Duplicate the top value on the stack.

    [line-feed][tab]: Swap the top two value on the stack.

    [line-feed][line-feed]: Discard the top value on the stack.

"""
PUSH_STACK = r'{SPACE}{NUMBER}'.format(NUMBER=NUMBER, **chars)
DUPLICATE_NTH = r'{TAB}{SPACE}{NUMBER}'.format(NUMBER=NUMBER, **chars)
DISCARD_TOP_N = r'{TAB}{LINE_FEED}{NUMBER}'.format(NUMBER=NUMBER, **chars)
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
MODULUS = r'{TAB}{TAB}'.format(**chars)

"""
IMP [tab][tab] - Heap Access

    [space]: Pop a and b, then store a at heap address b.

    [tab]: Pop a and then push the value at heap address a onto the stack.
"""
STORE = r'{SPACE}'.format(**chars)
RETRIEVE = r'{TAB}'.format(**chars)

"""
IMP [tab][line-feed] - Input/Output

    [space][space]: Pop a value off the stack and output it as a character.

    [space][tab]: Pop a value off the stack and output it as a number.

    [tab][space]: Read a character from input, a, Pop a value off the
    stack, b, then store the ASCII value of a at heap address b.

    [tab][tab]: Read a number from input, a, Pop a value off the stack, b, then
    store a at heap address b.
"""
POP_PRINT = r'{SPACE}{TAB}'.format(**chars)
POP_PRINT_CHR = r'{SPACE}{SPACE}'.format(**chars)
READ_CHAR = r'{TAB}{SPACE}'.format(**chars)
READ_NUMBER = r'{TAB}{TAB}'.format(**chars)

"""
IMP [line-feed] - Flow Control

    [space][space] (label): Mark a location in the program with label n.

    [space][tab] (label): Call a subroutine with the
    location specified by label n.

    [space][line-feed] (label): Jump unconditionally to the position specified
    by label n.

    [tab][space] (label): Pop a value off the stack and jump to the label
    specified by n if the value is zero.

    [tab][tab] (label): Pop a value off the stack and jump to the label
    specified by n if the value is less than zero.

    [tab][line-feed]: Exit a subroutine and return control to the location from
    which the subroutine was called.

    [line-feed][line-feed]: Exit the program.
"""
MARK_LOCATION = r'{SPACE}{SPACE}{LABEL}'.format(LABEL=LABEL, **chars)
CALL_SUBROUTINE = r'{SPACE}{TAB}{LABEL}'.format(LABEL=LABEL, **chars)
JUMP = r'{SPACE}{LINE_FEED}{LABEL}'.format(LABEL=LABEL, **chars)
JUMP_IF_ZERO = r'{TAB}{SPACE}{LABEL}'.format(LABEL=LABEL, **chars)
JUMP_IF_LT_ZERO = r'{TAB}{TAB}{LABEL}'.format(LABEL=LABEL, **chars)
EXIT_SUBROUTINE = r'{TAB}{LINE_FEED}'.format(**chars)
EXIT = r'{LINE_FEED}{LINE_FEED}'.format(**chars)

grammar = {
    STACK_MANIPULATION: {
        PUSH_STACK: push_stack,
        DUPLICATE_NTH: duplicate_nth,
        DISCARD_TOP_N: discard_top_n,
        DUPLICATE_TOP: duplicate_top,
        SWAP_FIRST_TWO: swap_first_two,
        DISCARD_TOP: discard_top,
    },
    ARITHMETIC: {
        ADDITION: addition,
        SUBTRACTION: subtraction,
        MULTIPLICATION: multiplication,
        DIVISION: division,
        MODULUS: modulo
    },
    HEAP_ACCESS: {
        STORE: heap_store,
        RETRIEVE: heap_retrieve,
    },
    IO: {
        POP_PRINT: pop_print,
        POP_PRINT_CHR: pop_print_chr,
        READ_CHAR: read_char,
        READ_NUMBER: read_number,
    },
    FLOW_CONTROL: {
        MARK_LOCATION: mark_location,
        CALL_SUBROUTINE: call_subroutine,
        JUMP: jump,
        JUMP_IF_ZERO: jump_if_zero,
        JUMP_IF_LT_ZERO: jump_if_lt_zero,
        EXIT_SUBROUTINE: exit_subroutine,
        EXIT: exit_program
    }
}
