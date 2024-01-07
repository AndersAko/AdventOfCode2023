import sys
from copy import deepcopy
from dataclasses import dataclass
from enum import IntEnum, auto, Enum
from pathlib import Path
from typing import Tuple, NamedTuple
from more_itertools import peekable
import re

class State(NamedTuple):
    row: int
    col: int
    path: list[Tuple[int,int]]

sys.setrecursionlimit(20000)

def longest_path1(state: State, map, visited) -> int:
    row, col = state.row,state.col
    path = state.path + [(row,col)]
    if row == len(map) - 1:
        # print (f"Reached end after going {path} = {len(path)}")
        return len(state.path)
    
    if map[row][col] == '>':
        return longest_path1(State(row, col + 1, path), map, visited)
    elif map[row][col] == 'v':
        return longest_path1(State(row + 1, col, path), map, visited)
    elif map[row][col] == '>':
        return longest_path1(State(row, col - 1, path), map, visited)
    elif map[row][col] == 'v':
        return longest_path1(State(row - 1, col, path), map, visited)
    possible_moves = [
        State(row + dr,col + dc, path)
        for dr in [-1,0,1] for dc in [-1,0,1] 
        if (dr==0 or dc==0) and dr != dc and map[row + dr][col + dc] != '#' and (row + dr,col + dc) not in path
            and not (dr == -1 and map[row + dr][col + dc] == 'v' or dr == 1 and map[row + dr][col + dc] == '^' 
                    or dc == -1 and map[row + dr][col + dc] == '>' or dc == 1 and map[row + dr][col + dc] == '<')
    ]
    longest = max((longest_path1(move, map, visited) for move in possible_moves), default=0)
    return longest

def solve1(map: list[str]) -> int:
    return longest_path1(State(0,1,[]), map, dict())

cardinal_directions = [ (dr,dc) for dr in [-1,0,1] for dc in [-1,0,1] if (dr==0 or dc==0) and dr != dc ]

def single_route(from_pos, coming_from, routes:dict, map:list[str]) -> None|Tuple[Tuple[int,int], Tuple[int,int], int]:
    """ If there is a single route possible from row, col (avoiding coming_from),
        return the end of that path, ie where there are multiple branching options or the end is reached:
            (row, col), coming_from, route_len
        Else: return None
    """
    # print(f"Single route from {from_pos}, {coming_from}", end='')
    if (from_pos, coming_from) not in routes:
        row1, col1 = from_pos
        route_len  = 0
        while True:
            possible_moves = [
                (row1 + dr,col1 + dc)
                for dr, dc in cardinal_directions
                if row1 + dr >= 0 and row1 + dr < len(map)
                and map[row1 + dr][col1 + dc] != '#'
                and (row1 + dr,col1 + dc) != coming_from
            ]
            if len(possible_moves) != 1: 
                break
                
            route_len += 1
            coming_from = (row1,col1)
            (row1, col1), = possible_moves
            if row1 == len(map) - 1 or row1 == 0:
                break

        if route_len == 0:
            return None
        routes[(from_pos, coming_from)] = ((row1, col1), coming_from, route_len)
    # print(f" leads to  {routes[(from_pos, coming_from)]}")
    return routes[(from_pos, coming_from)]


def longest_path2(state: State, routes:dict, map:list[str]) -> int | None:
    """
        Return the longest path possible from state, or None if no path is possible

        Assumes state is a valid position
    """
    # print(f"Checking state: {state}")

    row, col = state.row,state.col
    path = state.path + [(row,col)]
    if row == len(map) - 1:
        print (f"Reached end after going {path} = {len(path)}")
        return 0

    coming_from = path[-2]
    if (_single_route := single_route ((row,col), coming_from, routes, map)) is not None:
        (row1, col1), coming_from, route_len = _single_route
        if (row1, col1) in path:
            return None
        lp = longest_path2(State(row1,col1,path+[coming_from]), routes, map)
        return route_len + lp if lp is not None else None

    possible_moves = [
        (row + dr,col + dc)
        for dr, dc in cardinal_directions
        if row + dr >= 0 and row + dr < len(map)
        and map[row + dr][col + dc] != '#'
        and (row + dr,col + dc) != coming_from
        and (row + dr,col + dc) not in path
    ]
    longest = max( (lp for r,c in possible_moves
                    if (lp:=longest_path2(State(r,c,path), routes=routes, map=map)) is not None),
                    default=None
                 )
    # if longest is not None: 
        # print(f"Longest path from {row,col} is {longest} + 1 = {longest + 1}")
    return longest + 1 if longest is not None else None

def solve2(map: list[str]) -> int:
    lp = longest_path2(State(0,1,[(-1,0)]), routes=dict(), map=map)
    assert lp is not None
    return lp
        

def solve():
    with open(Path(__file__).with_name('input.txt'), 'r') as f:
        lines = f.read().split('\n')
        answer = solve1(lines)
        print (f"Part1: {answer}")

        answer = solve2(lines)
        print (f"Part2: {answer}")


if __name__ == '__main__': solve()