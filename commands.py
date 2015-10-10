
class StopProgram(Exception):
    def __init__(self):
        pass


def parse_digit(sign, digit):
    digit = digit or '0'
    digit = digit.replace(' ', '0').replace('\t', '1')
    sign = sign.replace(' ', '1').replace('\t', '-1')
    digit = int(sign) * int(digit, base=2)
    return digit


def push_stack(inp, output, stack, heap, sign=None, digit=None):
    assert digit is not None
    assert sign is not None
    stack.append(parse_digit(sign, digit))
    return inp, output


def duplicate_nth(inp, output, stack, heap, sign=None, digit=None):
    assert digit is not None
    assert sign is not None
    n = parse_digit(sign, digit)
    stack.append(stack[-n-1])
    return inp, output


def discard_top_n(inp, output, stack, heap, sign=None, digit=None):
    assert digit is not None
    assert sign is not None
    n = parse_digit(sign, digit)

    if n < 0 or n >= len(stack):
        stack = [stack[-1]]
    else:
        pass


def duplicate_top(inp, output, stack, heap):
    stack.append(stack[-1])
    return inp, output


def swap_first_two(inp, output, stack, heap):
    a = stack.pop()
    b = stack.pop()
    stack.append(a)
    stack.append(b)
    return inp, output


def discard_top(inp, output, stack, heap):
    stack.pop()
    return inp, output


def addition(inp, output, stack, heap):
    stack.append(stack.pop() + stack.pop())
    return inp, output


def subtraction(inp, output, stack, heap):
    a = stack.pop()
    b = stack.pop()
    stack.append(b - a)
    return inp, output


def multiplication(inp, output, stack, heap):
    stack.append(stack.pop() * stack.pop())
    return inp, output


def division(inp, output, stack, heap):
    a = stack.pop()
    b = stack.pop()
    stack.append(b // a)
    return inp, output


def modulo(inp, output, stack, heap):
    a = stack.pop()
    b = stack.pop()
    stack.append(b % a)
    return inp, output


def pop_print(inp, output, stack, heap):
    output += str(stack.pop())
    return inp, output


def pop_print_chr(inp, output, stack, heap):
    output += chr(int(stack.pop()))
    return inp, output


def exit_program(inp, output, stack, heap):
    raise StopProgram
