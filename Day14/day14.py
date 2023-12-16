from copy import deepcopy
from enum import IntEnum, auto, Enum
from pathlib import Path

class Dir(Enum):
    North = auto()
    East = auto()
    South = auto()
    West = auto()

def tilt(platform: list[list[str]], dir) -> list[list[str]]:
    if dir == Dir.North:
        for c in range(len(platform[0])):
            block = -1
            for r,_ in enumerate(platform):
                if platform[r][c] == 'O': 
                    platform[r][c] = '.'
                    platform[block + 1][c] = 'O'
                    block += 1
                elif platform[r][c] == '#':
                    block = r
    elif dir == Dir.East:
        for r in range(len(platform)):
            block = len(platform[0])
            for c in reversed(range(len(platform[0]))):
                if platform[r][c] == 'O': 
                    platform[r][c] = '.'
                    platform[r][block - 1] = 'O'
                    block -= 1
                elif platform[r][c] == '#':
                    block = c
    elif dir == Dir.South:
        for c in range(len(platform[0])):
            block = len(platform)
            for r in reversed(range(len(platform))):
                if platform[r][c] == 'O': 
                    platform[r][c] = '.'
                    platform[block - 1][c] = 'O'
                    block -= 1
                elif platform[r][c] == '#':
                    block = r
    elif dir == Dir.West:
        for r in range(len(platform)):
            block = -1
            for c in range(len(platform[0])):
                if platform[r][c] == 'O': 
                    platform[r][c] = '.'
                    platform[r][block + 1] = 'O'
                    block += 1
                elif platform[r][c] == '#':
                    block = c

def spin(platform: list[list[str]]):
    tilt(platform, Dir.North)
    tilt(platform, Dir.West)
    tilt(platform, Dir.South)
    tilt(platform, Dir.East)

def load(platform: list[list[str]]) -> int:
    load = 0
    for r,row in enumerate(platform):
        load += sum(len(platform)-r for c in row if c =='O')
    return load

def solve():
    with open(Path(__file__).with_name('input.txt'), 'r') as f:
        input_data = [ [c for c in l] for l in f.read().split('\n')]
        platform = deepcopy(input_data)
        print ('\n'.join(''.join(c for c in l) for l in platform), '\n')
        tilt(platform, Dir.North)
        print ('\n'.join(''.join(c for c in l) for l in platform), '\n')
        print(f"Part 1: load = {load(platform)}")

        platform = deepcopy(input_data)
        states = dict()
        for i in range(1,1000):
            spin(platform)
            key = tuple(tuple(r) for r in platform)
            if key in states:
                # Repeat state
                prev, l = states[key]
                repeat = i - prev
                offset = prev
                equiv_1000000000 = (1000000000 - offset) % repeat + offset
                load_1000000000 = next( l for c,l in states.values() if c == equiv_1000000000 )

                print (f"Cycle equivalent to 1000000000 = {equiv_1000000000} => {load_1000000000}")
                break
            else:
                states[key] = (i, load(platform))
                
            print(f"Spin cycle: {i} {states.values()}")
            print ('\n'.join(''.join(c for c in l) for l in platform), '\n')



if __name__ == '__main__': solve()