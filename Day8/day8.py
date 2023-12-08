from enum import IntEnum, auto, Enum
from pathlib import Path
from itertools import cycle
import math

def prep(line: str):
    line = ''.join(c for c in line if c.isalnum() or c.isspace())
    return [w for w in line.split(' ') if w != '']

def solve():
    with open(Path(__file__).with_name('input.txt'), 'r') as f:
        lines = f.read().split('\n')
        instructions = lines[0]

        network = { prep(line)[0]: (prep(line)[1], prep(line)[2]) for line in lines[2:]}
        
        # Part 1
        location = "AAA"
        print (location)
        steps = 0
        for instr in cycle(instructions):
            location = network[location][0] if instr == 'L' else network[location][1]
            steps += 1
            print (steps, instr, location)
            if location == 'ZZZ': break

        print(f"Total steps: {steps}")

        # Part 2
        locations = [ l for l in network.keys() if l.endswith('A')]
        steps = 0
        end_points = dict()
        instr_len = len(instructions)
        for instr in cycle(instructions):
            locations = [
                network[location][0] if instr == 'L' else network[location][1]
                for location in locations
            ]
            steps += 1
            if any(l.endswith('Z') for l in locations): 
                for l in locations:
                    if l.endswith('Z'):
                        last_same_point = end_points.get(l)
                        if last_same_point is None:
                             # first time
                            end_points[l] = (steps,None)
                        else:
                            if last_same_point[1] is None:  # Second time
                                diff = steps - last_same_point[0]
                                end_points[l] = (last_same_point[0], diff)
                            else:                       # third and subsequent times
                                assert (steps - last_same_point[0]) % instr_len == last_same_point[1] % instr_len
                print (steps, steps%instr_len, instr, locations, end_points)
            if len(end_points) == len(locations) and all(e[1] is not None for e in end_points.values()): break
            if all(l.endswith('Z') for l in locations): break

        print(f"Total steps, part 2:  => {math.lcm(*(s[1] for s in end_points.values()))}")

if __name__ == '__main__': solve()