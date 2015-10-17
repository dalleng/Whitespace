from __future__ import print_function

from commands import StopProgram, Jump
from grammar import grammar, comments

import re


class ParseError(Exception):
    def __init__(self, code):
        self.code = repr(code)

    def __str__(self):
        return repr(self.code)


class RepeatedLabels(ParseError):
    pass


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


def whitespace(code, inp='', debug=False):
    output = ''
    stack = []
    heap = {}
    program = []
    call_stack = []
    locations = {}

    # remove comments
    code = re.sub(comments, '', code)

    line = 0

    while code:
        code, func, kwargs = parse(code)

        if 'label' in kwargs:
            kwargs['locations'] = locations

        if func.__name__ in ('call_subroutine', 'exit_subroutine'):
            kwargs['call_stack'] = call_stack

        if func.__name__ == 'mark_location':
            if kwargs['label'] in locations:
                raise RepeatedLabels
            else:
                locations[kwargs['label']] = line

        program.append((func, kwargs))
        line += 1

        if debug:
            print('Parse:', func.__name__, kwargs)

    program_counter = 0

    while program_counter < len(program):
        try:
            func, kwargs = program[program_counter]
            inp, output = func(
                program_counter, inp, output, stack, heap, **kwargs)

            if debug:
                print('Exec:', func.__name__, kwargs)

        except StopProgram:
            return output
        except Jump as j:
            program_counter = j.line
        else:
            program_counter += 1

    raise RuntimeError('Unclean termination')
