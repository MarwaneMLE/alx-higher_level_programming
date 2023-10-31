#!/usr/bin/python3
def magic_string():
    if not hasattr(magic_string, 'calls'):
        magic_string.calls = 0
    magic_string.calls += 1
    return ', '.join(['BestSchool'] * magic_string.calls)
