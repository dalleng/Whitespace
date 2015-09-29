from __future__ import print_function

from commands import StopProgram
from grammar import grammar

import re
import sys

import pdb


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
            # print(func)
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
