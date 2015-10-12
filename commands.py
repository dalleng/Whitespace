
class StopProgram(Exception):
    pass


class InputError(Exception):
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

    if n < 0:
        raise IndexError

    stack.append(stack[-n-1])
    return inp, output


def discard_top_n(inp, output, stack, heap, sign=None, digit=None):
    assert digit is not None
    assert sign is not None
    n = parse_digit(sign, digit)

    if n < 0 or n >= len(stack):
        top = stack.pop()
        del stack[:]
        stack.append(top)
    else:
        stack_copy = stack[:]
        del stack[:]
        for i in range(0, len(stack_copy)-n-1):
            stack.append(stack_copy[i])
        stack.append(stack_copy[-1])

    return inp, output


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


def heap_retrieve(inp, output, stack, heap):
    a = stack.pop()
    stack.append(heap[a])
    return inp, output


def heap_store(inp, output, stack, heap):
    a = stack.pop()
    b = stack.pop()
    heap[b] = a
    return inp, output


def read_char(inp, output, stack, heap):
    if not inp:
        raise InputError

    a, inp = inp[0], inp[1:]
    b = stack.pop()
    heap[b] = ord(a)
    return inp, output


def read_number(inp, output, stack, heap):
    i = inp.find('\n')

    if i == -1:
        raise InputError

    try:
        a = int(inp[:i])
    except ValueError:
        try:
            a = int(inp[:i], base=16)
        except:
            raise InputError

    inp = inp[i+1:]
    b = stack.pop()
    heap[b] = a

    return inp, output


def pop_print(inp, output, stack, heap):
    output += str(stack.pop())
    return inp, output


def pop_print_chr(inp, output, stack, heap):
    output += chr(int(stack.pop()))
    return inp, output


def exit_program(inp, output, stack, heap):
    raise StopProgram
