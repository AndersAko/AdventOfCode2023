from enum import IntEnum, auto, Enum
from pathlib import Path
from itertools import cycle

def prep(line: str):
    line = ''.join(c for c in line if c.isalnum() or c.isspace())
    return [w for w in line.split(' ') if w != '']

def solve():
    with open(Path(__file__).with_name('input.txt'), 'r') as f:
        lines = f.read().split('\n')
        instructions = lines[0]

        network = { prep(line)[0]: (prep(line)[1], prep(line)[2]) for line in lines[2:]}
        
        # # Part 1
        # location = "AAA"
        # print (location)
        # steps = 0
        # for instr in cycle(instructions):
        #     location = network[location][0] if instr == 'L' else network[location][1]
        #     steps += 1
        #     print (steps, instr, location)
        #     if location == 'ZZZ': break

        # print(f"Total steps: {steps}")

        # Part 2
        locations = [ l for l in network.keys() if l.endswith('A')]
        steps = 0
        for instr in cycle(instructions):
            locations = [
                network[location][0] if instr == 'L' else network[location][1]
                for location in locations
            ]
            steps += 1
            if steps < 20 or any(l.endswith('Z') for l in locations): 
                print (steps, instr, locations)
            if all(l.endswith('Z') for l in locations): break

        print(f"Total steps, part 2: {steps}")

if __name__ == '__main__': solve()