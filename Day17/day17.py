from collections import namedtuple
from copy import deepcopy
from enum import IntEnum, auto, Enum
from pathlib import Path
from queue import PriorityQueue, Queue
from cProfile import Profile
from pstats import SortKey, Stats

class Dir(int, Enum):
    North = auto()
    East = auto()
    South = auto()
    West = auto()

Move = namedtuple("Move", "row,col,last_turn,dir,cost,path")

def moves(move: Move, cost_map) -> list[Move]:
    size_r = len(cost_map)
    size_c = len(cost_map[0])
    row, col, last_turn, dir, cost, path = move
    dirs = (d for d in Dir
            if (last_turn < 3 and d == dir 
                or (d in [Dir.West, Dir.East] and dir in [ Dir.North, Dir.South])
                or (d in [Dir.North, Dir.South] and dir in [Dir.West, Dir.East])
                or dir is None)
            and (d == Dir.North and row > 0 or
                 d == Dir.East and col < size_c - 1 or
                 d == Dir.South and row < size_r - 1 or
                 d == Dir.West and col > 0)
            )
    def next_move(d) -> Move:
        r = row - 1 if d == Dir.North else row + 1 if d == Dir.South else row
        c = col - 1 if d == Dir.West else col + 1 if d == Dir.East else col
        return Move(r,c, last_turn + 1 if d == dir or dir is None else 1, d, cost + int(cost_map[r][c]),
                     path + [(r,c)])
    return [ next_move(d) for d in dirs]

# def moves(move: Move, cost_map) -> list[Move]:
#     row, col, last_turn, dir, cost, path = move
#     dirs = [ dir ] if last_turn < 2 else []
#     dirs.extend([Dir.West, Dir.East] if dir == Dir.North or dir == Dir.South else
#                 [Dir.North, Dir.South] if dir == Dir.East or dir == Dir.West else [])
#     dirs = [ d for d in dirs if d == Dir.North and row > 0 or  
#                                 d == Dir.East and col < size_c - 1 or 
#                                 d == Dir.South and row < size_r - 1 or 
#                                 d == Dir.West and col > 0 ]
#     def next_move(d) -> Move:
#         r = row - 1 if d == Dir.North else row + 1 if d == Dir.South else row
#         c = col - 1 if d == Dir.West else col + 1 if d == Dir.East else col
#         return Move(r,c, last_turn + 1 if d == dir else 0, d, cost + int(cost_map[r][c]),[])
#                     # path + [(r,c)])
#     return [ next_move(d) for d in dirs]

def ultra_moves(move: Move, cost_map) -> list[Move]:
    size_r = len(cost_map)
    size_c = len(cost_map[0])
    row, col, last_turn, dir, cost, path = move
    dirs = (d for d in Dir 
            if (last_turn < 10 and d == dir 
                or (last_turn >= 4 and d in [Dir.West, Dir.East] and dir in [ Dir.North, Dir.South])
                or (last_turn >= 4 and d in [Dir.North, Dir.South] and dir in [Dir.West, Dir.East])
                or dir is None)
            and (d == Dir.North and row > 0 or  
                 d == Dir.East and col < size_c - 1 or 
                 d == Dir.South and row < size_r - 1 or 
                 d == Dir.West and col > 0)
            )
    def next_move(d) -> Move:
        r = row - 1 if d == Dir.North else row + 1 if d == Dir.South else row
        c = col - 1 if d == Dir.West else col + 1 if d == Dir.East else col
        return Move(r,c, last_turn + 1 if d == dir or dir is None else 1, d, cost + int(cost_map[r][c]),
                     path + [(r,c)])
    return [ next_move(d) for d in dirs]


def part1(cost_map) -> Move:
    size_r = len(cost_map)
    size_c = len(cost_map[0])
    visited = dict()
    to_check = PriorityQueue()
    # Start pos = 0,0
    to_check.put((remain_cost(0,0,size_r, size_c), Move(0,0,1,None,0,[])))
    while not to_check.empty():
        # Pick lowest
        _,next = to_check.get()
        if (next.row,next.col,next.last_turn,next.dir) in visited and next.cost >= visited[(next.row,next.col,next.last_turn,next.dir)]:
            continue
        visited[(next.row,next.col,next.last_turn, next.dir)] = next.cost
        if len(visited) % 50000 == 0: 
            print(f"Checked: {len(visited)}")
            print_move(next, cost_map)
        if next.row == size_r - 1 and next.col == size_c - 1:
            # If at target = bottom right => quit
            print(f"Part 1: Found a way with {next.cost} in heatloss after checking {len(visited)} states")
            print_move(next, cost_map)
            break
        # Place all next moves in queue
        possible = moves(next, cost_map)
        for m in possible:
            if not (m.row,m.col,m.last_turn,m.dir) in visited or visited[(m.row,m.col,m.last_turn,m.dir)] >= m.cost:
                to_check.put((m.cost + remain_cost(m.row,m.col,size_r, size_c), m))
    return next

def part2(cost_map) -> Move:
    # Part 2
    size_r = len(cost_map)
    size_c = len(cost_map[0])

    print("Part2")
    visited = dict()
    to_check = PriorityQueue()
    best = None
    # Start pos = 0,0
    to_check.put((remain_cost(0,0,size_r, size_c), Move(0,0,0,None,0,[(0,0)])))
    while not to_check.empty():
        # Pick lowest
        _,next = to_check.get()
        if (next.row,next.col,next.last_turn,next.dir) in visited and next.cost >= visited[(next.row,next.col,next.last_turn,next.dir)]:
            continue
        visited[(next.row,next.col,next.last_turn, next.dir)] = next.cost
        if len(visited) % 50000 == 0: 
            print(f"Checked: {len(visited)}")
            print_move(next, cost_map)
        if next.row == size_r - 1 and next.col == size_c - 1 and next.last_turn>=4:
            # If at target = bottom right => quit
            print(f"Part 2: Found a way with {next.cost} in heatloss after checking {len(visited)} states")
            print_move(next, cost_map)
            if best is None or next.cost < best.cost:   
                best = next
            # break
        # Place all next moves in queue
        possible = ultra_moves(next, cost_map)
        for m in possible:
            if not (m.row,m.col,m.last_turn,m.dir) in visited or visited[(m.row,m.col,m.last_turn,m.dir)] > m.cost:
                to_check.put((m.cost + remain_cost(m.row,m.col,size_r, size_c), m))
    return best

def print_move(m, cost_map):
    size_r = len(cost_map)
    size_c = len(cost_map[0])
    print('\n'.join(''.join(
        ('<' if m.dir == Dir.West else '^' if m.dir==Dir.North else '>' if m.dir==Dir.East else 'v')
        if m.row == r and m.col==c else
        '.' if (r,c) in m.path else
        cost_map[r][c] for c in range(size_c)) for r in range(size_r)))
    print(f"{m.cost} ({m.cost + remain_cost(m.row,m.col,size_r, size_c)})\n")

def remain_cost(r, c, size_r, size_c) -> int:
    return size_r - r - 1 + size_c - c - 1

def solve():

    with open(Path(__file__).with_name('input.txt'), 'r') as f:
        cost_map = f.read().split('\n')
        print(f"Part 1: Best route heatloss = {part1(cost_map).cost}")
        print(f"Part 2: Best route heatloss = {part2(cost_map).cost}")


if __name__ == '__main__': solve()
    # with Profile() as profile:
    #     solve()
    #     (
    #         Stats(profile)
    #         .strip_dirs()
    #         .sort_stats(SortKey.CALLS)
    #         .print_stats()
    #     )