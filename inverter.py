"""
A small script used to invert a linear sequence of assembly instructions.

Python version:
    3.4.2

Usage:
    py inverter.py file.asm
"""

import json
import sys

MIRROR_FILE = 'mirror.json'

def load_mirror():
    """Returns a dict, mapping instuctions to opposite instructions."""
    with open(MIRROR_FILE) as mirror_file:
        return json.load(mirror_file)

def invert(instruction, mirror):
    """Returns the opposite (if exists) of an instruction."""
    if instruction in mirror:
        return mirror[instruction]
    return instruction

def main():
    """Entry point."""
    if len(sys.argv) != 2:
        print('Usage: py', sys.argv[0], 'file.asm')
        return

    lines = []
    with open(sys.argv[1], 'r') as asm_file:
        for line in asm_file:
            if line:
                lines.append(line.strip())
    lines.reverse()
    mirror = load_mirror()
    for line in lines:
        instruction = line.split()
        instruction[0] = invert(instruction[0], mirror)
        print(' '.join(instruction))

main()
