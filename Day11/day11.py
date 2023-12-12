from enum import IntEnum, auto, Enum
from pathlib import Path


def dist(from_pos, to_pos, expand, factor):
    if from_pos < to_pos: 
        low = from_pos
        high = to_pos
    else:
        high = from_pos
        low = to_pos
    return high-low + sum(factor for x in expand if x > low and x < high)

def solve():
    with open(Path(__file__).with_name('input.txt'), 'r') as f:
        lines = f.read().split('\n')

        galaxies = [ (c,r) for r,line in enumerate(lines) for c,char in enumerate(line) if char == '#']
        empty_rows = [ r for r,l in enumerate(lines) if '#' not in l]
        empty_cols = [ c for c,_ in enumerate(lines[0]) if all(l[c]!='#' for l in lines) ]
        print(galaxies, empty_cols, empty_rows)

        sum_distance1 = 0
        for index, galaxy in enumerate(galaxies):
            for second_index in range(index+1, len(galaxies)):
                distance = (dist(galaxies[index][0], galaxies[second_index][0], empty_cols, 1) +
                            dist(galaxies[index][1], galaxies[second_index][1], empty_rows, 1))

                sum_distance1 += distance
                # print(f"Galaxy @{galaxy} to {galaxies[second_index]} = {distance}   => {sum_distance}")

        print(f"Part1: Total distance: {sum_distance1}")

        sum_distance2 = 0
        for index, galaxy in enumerate(galaxies):
            for second_index in range(index+1, len(galaxies)):
                distance = (dist(galaxies[index][0], galaxies[second_index][0], empty_cols, 1000000-1) +
                            dist(galaxies[index][1], galaxies[second_index][1], empty_rows, 1000000-1))

                sum_distance2 += distance
                # print(f"Galaxy @{galaxy} to {galaxies[second_index]} = {distance}   => {sum_distance}")

        print(f"Part2: Total distance: {sum_distance2}")

if __name__ == '__main__': solve()