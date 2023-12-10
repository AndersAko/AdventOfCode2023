from enum import IntEnum, auto, Enum
from pathlib import Path
from itertools import cycle
import math

class Dir(int, Enum):
    North = auto()
    East = auto()
    South = auto()
    West = auto()

class Side(int,Enum):
    Left = 1
    Right = 2
    Loop = 3
    Other = 4

"""
| is a vertical pipe connecting north and south.
- is a horizontal pipe connecting east and west.
L is a 90-degree bend connecting north and east.
J is a 90-degree bend connecting north and west.
7 is a 90-degree bend connecting south and west.
F is a 90-degree bend connecting south and east.
. is ground; there is no pipe in this tile."""

def find_start(lines) -> (int,int,Dir):
        (sx, sy), = ( (l.find('S'),i) for i,l in enumerate(lines) if 'S' in l) # (x,y)
        print (f"Starting point: {sx}, {sy}") 
        
        # Find entry point
        for dir in Dir:
            x,y,dir = move_and_turn(sx, sy, dir, lines)
            if dir is not None: 
                return x,y,dir
        print ("Didn't find start!!")                

def move_and_turn(x,y,dir,lines) -> (int,int,Dir):
    if dir is Dir.North and y>0:
        pipe = lines[y-1][x]
        return x, y-1, Dir.North if pipe == '|' else Dir.West if pipe == '7' else Dir.East if pipe == 'F' else None
    if dir is Dir.East:
        pipe = lines[y][x+1]
        return (x+1, y, Dir.East if pipe == '-' else Dir.South if pipe == '7' else Dir.North if pipe == 'J' else None)
    if dir is Dir.South:
        pipe = lines[y+1][x]
        return (x, y+1, Dir.South if pipe == '|' else Dir.East if pipe == 'L' else Dir.West if pipe == 'J' else None)
    if dir is Dir.West and x>0:
        pipe = lines[y][x-1]
        return (x-1, y, Dir.West if pipe == '-' else Dir.North if pipe == 'L' else Dir.South if pipe == 'F' else None)
    return None,None,None

def is_inside(x,loop_line,clock_wise):
    if loop_line[x] is not Side.Other: return False
    for i in range(x+1,len(loop_line)):
        if loop_line[i] is Side.Left:
            return not clock_wise
        if loop_line[i] is Side.Right:
            return clock_wise
        if loop_line[i] is Side.Loop:
            print("Surprise!", x,i,loop_line[i], loop_line)
    return False

def solve():
    with open(Path(__file__).with_name('input.txt'), 'r') as f:
        lines = f.read().split('\n')
        loop = [[Side.Other for _ in l] for l in lines]
        pos_x, pos_y, dir = find_start(lines)
        loop[pos_y][pos_x] = Side.Loop

        length = 1
        turns = 0
        while lines[pos_y][pos_x] != 'S':
            prev_dir = dir
            pos_x, pos_y, new_dir = move_and_turn(pos_x, pos_y, dir, lines)
            loop[pos_y][pos_x] = Side.Left if Dir.North in [dir, new_dir] else Side.Right if Dir.South in [dir, new_dir] else Side.Loop
            dir = new_dir
            turns += (dir-prev_dir + 2) % 4 - 2 if dir is not None else 0
            length += 1
            print(pos_x, pos_y, dir)
        print (f"Length {length} => {length//2}")
        print (f"Turns: {turns}")

        print ( "Loop")
        print ( "\n".join("".join(
            'O' if c is Side.Other else 'L' if c is Side.Left else 'R' if c is Side.Right else 'X' for c in l) for l in loop) )
        print()

        inside_cells = [['X' if c is Side.Loop else 'I' if is_inside(i,l, turns > 0) else 'O' for i,c in enumerate(l)]  for l in loop]
        print (  "\n".join("".join(c for c in l) for l in inside_cells) )

        print (sum(sum(1 for c in l if c=='I') for l in inside_cells))

if __name__ == '__main__': solve()

"""
1   1=0 2=1 4=-1*
2   1=-1 2=0 3=1
3   2=-1, 3=0, 4=1
4   3=-1 4=0 1=-1*

0   0=0 1=1 3=-1
1   0=-1 1=0 2=1
2   1=-1, 2=0, 3=1
3   2=-1 3=0 0=-1

"""