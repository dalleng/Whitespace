
class StopProgram(Exception):
    pass


class InputError(Exception):
    pass


class Jump(Exception):
    def __init__(self, line):
        self.line = line


def parse_digit(sign, digit):
    digit = digit or '0'
    digit = digit.replace(' ', '0').replace('\t', '1')
    sign = sign.replace(' ', '1').replace('\t', '-1')
    digit = int(sign) * int(digit, base=2)
    return digit


def push_stack(line, inp, output, stack, heap, sign=None, digit=None):
    assert digit is not None
    assert sign is not None
    stack.append(parse_digit(sign, digit))
    return inp, output


def duplicate_nth(line, inp, output, stack, heap, sign=None, digit=None):
    assert digit is not None
    assert sign is not None
    n = parse_digit(sign, digit)

    if n < 0:
        raise IndexError

    stack.append(stack[-n-1])
    return inp, output


def discard_top_n(line, inp, output, stack, heap, sign=None, digit=None):
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


def duplicate_top(line, inp, output, stack, heap):
    stack.append(stack[-1])
    return inp, output


def swap_first_two(line, inp, output, stack, heap):
    a = stack.pop()
    b = stack.pop()
    stack.append(a)
    stack.append(b)
    return inp, output


def discard_top(line, inp, output, stack, heap):
    stack.pop()
    return inp, output


def addition(line, inp, output, stack, heap):
    stack.append(stack.pop() + stack.pop())
    return inp, output


def subtraction(line, inp, output, stack, heap):
    a = stack.pop()
    b = stack.pop()
    stack.append(b - a)
    return inp, output


def multiplication(line, inp, output, stack, heap):
    stack.append(stack.pop() * stack.pop())
    return inp, output


def division(line, inp, output, stack, heap):
    a = stack.pop()
    b = stack.pop()
    stack.append(b // a)
    return inp, output


def modulo(line, inp, output, stack, heap):
    a = stack.pop()
    b = stack.pop()
    stack.append(b % a)
    return inp, output


def heap_retrieve(line, inp, output, stack, heap):
    a = stack.pop()
    stack.append(heap[a])
    return inp, output


def heap_store(line, inp, output, stack, heap):
    a = stack.pop()
    b = stack.pop()
    heap[b] = a
    return inp, output


def read_char(line, inp, output, stack, heap):
    if not inp:
        raise InputError

    a, inp = inp[0], inp[1:]
    b = stack.pop()
    heap[b] = ord(a)
    return inp, output


def read_number(line, inp, output, stack, heap):
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


def pop_print(line, inp, output, stack, heap):
    output += str(stack.pop())
    return inp, output


def pop_print_chr(line, inp, output, stack, heap):
    output += chr(int(stack.pop()))
    return inp, output


def mark_location(line, inp, output, stack, heap, **kwargs):
    return inp, output


def call_subroutine(line, inp, output, stack, heap,
                    call_stack=None,
                    label=None,
                    locations=None):
    assert label is not None
    assert call_stack is not None
    call_stack.append(line)
    raise Jump(locations[label])


def jump(line, inp, output, stack, heap, label=None, locations=None):
    assert label is not None
    raise Jump(locations[label])


def jump_if_zero(line, inp, output, stack, heap, label=None, locations=None):
    assert label is not None

    if stack.pop() == 0:
        raise Jump(locations[label])

    return inp, output


def jump_if_lt_zero(line, inp, output, stack, heap,
                    label=None,
                    locations=None):
    assert label is not None

    if stack.pop() < 0:
        raise Jump(locations[label])

    return inp, output


def exit_subroutine(line, inp, output, stack, heap, call_stack=None):
    assert call_stack is not None
    raise Jump(call_stack.pop() + 1)


def exit_program(line, inp, output, stack, heap):
    raise StopProgram
