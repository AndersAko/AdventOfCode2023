from collections import namedtuple
from copy import deepcopy
from enum import IntEnum, auto, Enum
from pathlib import Path
from queue import PriorityQueue, Queue
from cProfile import Profile
from pstats import SortKey, Stats

def pos_from(pos, garden_map) -> list:
    row,col = pos
    possible = [(r,c) for r,c in [(row+1,col), (row-1,col), (row,col-1), (row,col+1)]
                if garden_map[r][c] != '#']
    return possible

def possible_locations_from(pos, steps, visited, garden_map):
    if steps == 0: return {pos}
    if (pos,steps) in visited:  return visited[(pos,steps)]
    result = set.union(*(possible_locations_from(p,steps-1,visited, garden_map) for p in pos_from(pos, garden_map)))
    visited[(pos,steps)] = result
    return result

def solve1(input, steps: int) -> int:
    starting_pos, = ((r,l.index('S')) for r,l in enumerate(input) if 'S' in l)
    visited = dict()
    result = possible_locations_from(starting_pos, steps, visited, input)
    return len(result)

def solve():

    with open(Path(__file__).with_name('input.txt'), 'r') as f:
        garden_map = f.read().split('\n')
        print(f"Part 1: Unique plots visited in 64 steps:  {solve1(garden_map, 64)}")


if __name__ == '__main__': solve()
