from copy import deepcopy
from enum import IntEnum, auto, Enum
from pathlib import Path
import re

class Side(Enum):
    GoingIn = 1
    Inside = 2
    GoingOut = 3
    Outside = 4

def print_trench(trench: dict):
    min_r = min(r for r,_ in trench)
    min_c = min(c for _,c in trench)
    max_r = max(r for r,_ in trench)
    max_c = max(c for _,c in trench)
    print("\n".join("".join(trench[(r,c)][1] if (r,c) in trench else '.' for c in range(min_c, max_c+1)) for r in range(min_r,max_r+1)))

def solve1(input: list[str]) -> int:
    trench = dict()
    plan_re = re.compile(r"(\w) (\d+) \((#.*)\)")
    row,col = 0,0
    for line in input:
        dir,length,color = plan_re.findall(line)[0] 
        for i in range(int(length)):
            if dir == 'R':
                col += 1
            elif dir == 'D':
                c,_ = trench[(row,col)]
                trench[(row,col)] = (c,'D')
                row += 1
            elif dir == 'L':
                col -= 1
            elif dir == 'U':
                c,_ = trench[(row,col)]
                trench[(row,col)] = (c,'U')
                row -= 1
            else: 
                print(f"Unknown dir {dir}") 
            trench[(row,col)] = (color,dir)
                
    min_r = min(r for r,_ in trench)
    min_c = min(c for _,c in trench)
    max_r = max(r for r,_ in trench)
    max_c = max(c for _,c in trench)
    print_trench(trench)

    inside = False
    last_dir = None
    count = 0
    for r in range(min_r, max_r+1):
        for c in range(min_c, max_c+1):
            if (r,c) in trench:
                _,d = trench[(r,c)]
                if d in ['U', 'D']:
                    if d != last_dir:
                        inside = not inside
                    last_dir = d
                count += 1
            elif inside:
                trench[(r,c)] = (None,'I')
                count += 1
    print(f"Total size of pit: {count}")
    # print_trench(trench)

    return count


def solve2(input: list[str]) -> int:
    trench = dict()
    plan_re = re.compile(r"\w \d+ \(#(\w+)\)")
    row,col = 0,0
    for line in input:
        instruction = plan_re.findall(line)[0]
        length = int(instruction[:-1],16)
        dir = instruction[-1:]
        for i in range(int(length)):
            if dir == '0':
                col += 1
            elif dir == '1':
                trench[(row,col)] = 'D'
                row += 1
            elif dir == '2':
                col -= 1
            elif dir == '3':
                trench[(row,col)] = 'U'
                row -= 1
            else: 
                print(f"Unknown dir {dir}") 
            trench[(row,col)] = dir
                
    min_r = min(r for r,_ in trench)
    min_c = min(c for _,c in trench)
    max_r = max(r for r,_ in trench)
    max_c = max(c for _,c in trench)
    print (f"Trench limits: {(min_c, min_r)} -> {(max_c,max_r)}")

    inside = False
    last_dir = None
    count = 0
    for r in range(min_r, max_r+1):
        for c in range(min_c, max_c+1):
            if (r,c) in trench:
                d = trench[(r,c)]
                if d in ['U', 'D', '1', '3']:
                    if d != last_dir:
                        inside = not inside
                    last_dir = d
                count += 1
            elif inside:
                trench[(r,c)] = (None,'I')
                count += 1
    print(f"Total size of pit: {count}")
    # print_trench(trench)

    return count


def solve():
    with open(Path(__file__).with_name('input.txt'), 'r') as f:
        lines = f.read().split('\n')
        answer = solve1(lines)
        print (f"Part1: {answer}")

        # answer = solve2(line)
        # print (f"Part2: {answer}")



if __name__ == '__main__': solve()