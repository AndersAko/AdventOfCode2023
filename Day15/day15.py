from copy import deepcopy
from enum import IntEnum, auto, Enum
from pathlib import Path
import re

def hash(string: str) -> int:
    value = 0
    for c in string:
        value += ord(c)
        value *= 17 
        value %= 256
    return value

def run_step(step: str, boxes: dict) -> dict:
    pattern = re.compile(r"([^=-]+)(=|-)(\d*)")
    label,operation,focal = pattern.findall(step)[0]
    box_nr = hash(label)
    if operation == '-':
        if box_nr in boxes:
            existing_index = next((i for i,(l,_) in enumerate(boxes[box_nr]) if l == label), None)
            if existing_index is not None: 
                del boxes[box_nr][existing_index]
    elif operation == '=':
        if not box_nr in boxes:
            boxes[box_nr] = []

        existing_index = next((i for i,(l,_) in enumerate(boxes[box_nr]) if l == label), None)
        if existing_index is not None:
            boxes[box_nr][existing_index] = (label, int(focal))
        else: 
            boxes[box_nr].append((label, int(focal)))
    return boxes      

def solve1(input: str) -> int:
    return sum(hash(s) for s in input.split(','))

def solve2(input: str) -> int:
    boxes = dict()
    for step in input.split(','):
        boxes = run_step(step, boxes)

    answer = sum((b+1)*(s+1)*f for b in boxes for s,(l,f) in enumerate(boxes[b]))
    return answer

def solve():
    with open(Path(__file__).with_name('input.txt'), 'r') as f:
        line = f.read()
        answer = solve1(line)
        print (f"Part1: {answer}")

        answer = solve2(line)
        print (f"Part2: {answer}")



if __name__ == '__main__': solve()