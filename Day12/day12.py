from enum import IntEnum, auto, Enum
from pathlib import Path
import cProfile
import re

def matches(spring_map: str, spring_list: list[int]) -> int:
    # sum of numbers > remaining # and ? => 0   (failed to match)
    # sum of numbers < remaining # => 0   (failed to match)
    if spring_list==[] and spring_map=="": return 1
    if (sum(spring_list) > sum(1 for s in spring_map if s in "#?")
        or sum(spring_list) < sum(1 for s in spring_map if s in "#")
        or sum(s+1 for s in spring_list)-1 > len(spring_map)):
        return 0
    sum_matches = 0
    # Match first number
    if (spring_list and all(s in "#?" for s in spring_map[:spring_list[0]])
        and (len(spring_map)==spring_list[0] or spring_map[spring_list[0]] in ".?")):
        sum_matches += matches(spring_map[spring_list[0]+1:], spring_list[1:])
    if spring_map[0] in "?.":
        sum_matches += matches(spring_map[1:], spring_list)

    return sum_matches

def solve():
    with open(Path(__file__).with_name('input.txt'), 'r') as f:
        lines = f.read().split('\n')
        sum_matches = 0
        for line in lines:
            spring_map, spring_list = line.split(' ') 
            spring_list = [int(s) for s in spring_list.split(',')]

            num_matches = matches(spring_map, spring_list)
            sum_matches += num_matches
            print (f"{line} => {num_matches} matches")

        print(f"Part 1: Sum {sum_matches}")

        sum_matches = 0
        for line in lines:
            spring_map, spring_list = line.split(' ') 
            spring_list = [int(s) for s in spring_list.split(',')]
            spring_map = '?'.join(spring_map for i in range(5))
            spring_list = [s for i in range(5) for s in spring_list]
            num_matches = matches(spring_map, spring_list)
            print (f"{spring_map}, {spring_list} => {num_matches} matches")
            sum_matches += num_matches

        print(f"Part 2: Sum {sum_matches}")


if __name__ == '__main__': 
    solve()