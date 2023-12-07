from math import ceil, floor, sqrt
from pathlib import Path

def solve():
    with open(Path(__file__).with_name('input1.txt'), 'r') as f:
        lines = f.read().split('\n')

        # part 1
        times = [ int(t) for t in lines[0].split(' ')[1:] if t != '']
        records = [ int(d) for d in lines[1].split(' ')[1:] if d != '']
        result = 1
        for race in range(len(times)):
            t = times[race]
            r = records[race]
            lower_b = ceil(t/2 - sqrt(t*t/4 - r) + 1e-10)
            upper_b = floor(t/2 + sqrt(t*t/4 - r) - 1e-10)
            options = upper_b - lower_b + 1
            result *= options
            print (f"Race {race}: lower: {lower_b} upper: {upper_b} => {options} => {result}")


        # Part 2
        time = int(lines[0].split(':')[1].replace(' ', ''))
        dist = int(lines[1].split(':')[1].replace(' ',''))
        lower_b = ceil(time/2 - sqrt(time*time/4 - dist) + 1e-10)
        upper_b = floor(time/2 + sqrt(time*time/4 - dist) - 1e-10)
        options = upper_b - lower_b + 1

        print (f"Options for big race: {lower_b} - {upper_b} = {options}")
        
if __name__ == '__main__': solve()