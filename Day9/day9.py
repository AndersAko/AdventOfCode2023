from enum import IntEnum, auto, Enum
from pathlib import Path
from itertools import cycle
import math

def reduce_sequence(seq: list[int]) -> list[int]:
    return [ seq[i+1] - seq[i] for i in range(len(seq)-1)]

def solve():
    with open(Path(__file__).with_name('input.txt'), 'r') as f:
        lines = f.read().split('\n')
        result1 = 0
        result2 = 0
        for line in lines:
            seq = [int(n) for n in line.split(' ') if n != '']
            last_numbers = seq[-1:]
            first_numbers = [seq[0]]
            seq_len = len(seq)
            while not all(n==0 for n in seq):
                seq = reduce_sequence(seq)
                last_numbers.extend(seq[-1:])
                first_numbers.append(seq[0])
                print(seq, 'last: ', last_numbers)
            next_number = sum(last_numbers)
            print(f"{line} => {next_number}")
            result1 += next_number

            first_numbers.reverse()
            prev_number = 0
            for n in first_numbers:
                prev_number = n - prev_number
            result2 += prev_number

        print (f"Part 1: {result1}")
        print (f"Part 2: {result2}")

if __name__ == '__main__': solve()