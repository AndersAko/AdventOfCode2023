from copy import deepcopy
from enum import IntEnum, auto, Enum
from pathlib import Path

class Dir(int, Enum):
    North = auto()
    East = auto()
    South = auto()
    West = auto()

def beam(lines, row, col, dir:Dir, energized:set) -> set:
    while True:
        # Move
        if dir == Dir.North:
            if row == 0: return energized
            row -= 1
        elif dir == Dir.East:
            if col == len(lines[0])-1: return energized        
            col += 1
        elif dir == Dir.South:
            if row == len(lines)-1: return energized
            row += 1
        elif dir == Dir.West:
            if col == 0: return energized        
            col -= 1

        # Register location
        if (row,col,dir) in energized: return energized
        energized.add((row,col,dir))
        # print_beams(energized)

        # Check sign: split and turn
        if dir == Dir.North:
            if lines[row][col] == '\\':     dir = Dir.West
            elif lines[row][col] == '/':    dir = Dir.East
            elif lines[row][col] == '-':
                dir = Dir.East
                if col > 0: 
                    energized = beam(lines, row, col, Dir.West, energized)
        elif dir == Dir.East:
            if lines[row][col] == '\\':     dir = Dir.South
            elif lines[row][col] == '/':    dir = Dir.North
            elif lines[row][col] == '|':
                dir = Dir.South
                if row > 0:
                    energized = beam(lines, row, col, Dir.North, energized)
        elif dir == Dir.South:
            if lines[row][col] == '\\':     dir = Dir.East
            elif lines[row][col] == '/':    dir = Dir.West
            elif lines[row][col] == '-':
                dir = Dir.East
                if col > 0:
                    energized = beam(lines, row, col, Dir.West, energized)
        elif dir == Dir.West:
            if lines[row][col] == '\\':     dir = Dir.North
            elif lines[row][col] == '/':    dir = Dir.South
            elif lines[row][col] == '|':
                dir = Dir.South
                if row > 0:
                    energized = beam(lines, row, col, Dir.North, energized)

def print_beams(energized):
    def cell(row,col)->str:
        e = sum(1 for r,c,d in energized if r==row and c==col)
        return '.' if e == 0 else str(e)
    print('\n'.join(''.join(cell(r,c) for c in range(size_c)) for r in range(size_r)), '\n')

def solve():
    with open(Path(__file__).with_name('input.txt'), 'r') as f:
        lines = f.read().split('\n')
        global size_r, size_c
        size_r = len(lines)
        size_c = len(lines[0])
        energized = beam(lines, 0, -1, Dir.East, set())
        unique = {(r,c) for r,c,_ in energized}
        print(f"Part 1 - Energized cells: {len(unique)}")

        max_energized = 0
        for r in range(size_r):
            num_energized = len({(r,c) for r,c,_ in beam(lines, r, -1, Dir.East, set())})
            if num_energized > max_energized: max_energized = num_energized

            num_energized = len({(r,c) for r,c,_ in beam(lines, r, size_c, Dir.West, set())})
            if num_energized > max_energized: max_energized = num_energized
        for c in range(size_c):
            num_energized = len({(r,c) for r,c,_ in beam(lines, -1, c, Dir.South, set())})
            if num_energized > max_energized: max_energized = num_energized

            num_energized = len({(r,c) for r,c,_ in beam(lines, size_r, c, Dir.North, set())})
            if num_energized > max_energized: max_energized = num_energized

        print(f"Part2 : Maximum energization: {max_energized}")

if __name__ == '__main__': solve()