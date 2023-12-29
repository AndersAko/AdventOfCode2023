from copy import deepcopy
from enum import IntEnum, auto, Enum
from pathlib import Path
from more_itertools import peekable
import re

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


def solve2(input: list[str], long_input: bool) -> int:
    trench_cols = list()
    trench_rows = list()
    plan_re = re.compile(r"(\w) (\d+) \(#(\w+)\)")
    row,col = 0,0
    for line in input:
        d1, l1, instruction = plan_re.findall(line)[0]
        if long_input:
            length = int(instruction[:-1],16)
            dir = instruction[-1:]
        else:
            length = int(l1)
            dir = d1
        if dir in  ['0', 'R']:
            trench_rows.append((row, col, col + length))
            col += length
        elif dir in ['1', 'D']:
            trench_cols.append((col,row, row + length, 'D'))
            row += length
        elif dir in ['2', 'L']:
            trench_rows.append((row, col - length, col))
            col -= length
        elif dir in ['3', 'U']:
            trench_cols.append((col, row - length, row, 'U'))
            row -= length
                
    min_r = min(r for _,r,_,_ in trench_cols)
    min_c = min(c for c,_,_,_ in trench_cols)
    max_r = max(r for _,_,r,_ in trench_cols)
    max_c = max(c for c,_,_,_ in trench_cols)
    print (f"Trench limits: {(min_c, min_r)} -> {(max_c,max_r)}")

    row_breaks = peekable(sorted(list({r for _,r,_,_ in trench_cols}.union({r for _,_,r,_ in trench_cols}))))

    count = 0
    inside = False
    for row in row_breaks:
        intersects = peekable(sorted([(c,d) for c,r1,r2,d in trench_cols if r1<=row<=r2]))
        this_line_count = 0
        while True:
            this_c, this_d = next(intersects, (None, None))
            if this_c is None: 
                break
            next_c, next_d = intersects.peek((None, None))
            if not inside:
                if next_d == this_d:
                    start_col = next_c
                    next(intersects)
                else:
                    start_col = this_c
            else:
                if next_d == this_d:
                    this_line_count += this_c - start_col + 1
                    next(intersects)
                # elif next_c and (this_c, r) in ((c1,r1) for c1,r1,_,_ in trench_cols):
                #     this_line_count += next_c - start_col
                else: 
                    this_line_count += this_c - start_col + 1
            inside = not inside
        # Add all horizontal parts as inside
        this_line_count += sum(c2-c1-1 for (r1,c1,c2) in trench_rows if r1 == row)  

        assert not inside 
        count += this_line_count

        if row_breaks.peek(None) is not None:
            repeat_line_count = 0
            intersects = sorted([c for c,r1,r2,d in trench_cols if r1<=row+1<=r2])
            assert all((c,row+1) not in ((cc,r1) for cc,r1,_,_ in trench_cols) and (c,row+1) not in ((cc,r2) for cc,_,r2,_ in trench_cols)  for c in intersects)
            for col in intersects:
                if not inside:
                    start_col = col 
                else:
                    repeat_line_count += col - start_col + 1
                inside = not inside
            repeat_row = (row_breaks.peek() - row - 1 )
            count += repeat_row * repeat_line_count

    print(f"Total size of pit: {count}")
    # print_trench(trench)

    return count


def solve():
    with open(Path(__file__).with_name('input.txt'), 'r') as f:
        lines = f.read().split('\n')
        answer = solve1(lines)
        print (f"Part1: {answer}")

        answer = solve2(lines, True)
        print (f"Part2: {answer}")



if __name__ == '__main__': solve()