
class StopProgram(Exception):
    def __init__(self):
        pass


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
