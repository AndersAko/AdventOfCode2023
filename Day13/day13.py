from enum import IntEnum, auto, Enum
from pathlib import Path

def is_reflected_h(rows_before: int, pattern: list[str]) -> bool:
    rows = min(rows_before, len(pattern)-rows_before)
    return all(pattern[rows_before-i-1] == pattern[rows_before+i] for i in range(rows))

def smudge_reflected_h(rows_before: int, pattern: list[str]) -> int:
    rows = min(rows_before, len(pattern)-rows_before)
    diff = sum( sum(r1!=r2 for (r1, r2) in zip(pattern[rows_before-i-1],pattern[rows_before+i])) for i in range(rows))
    return diff

def is_reflected_v(cols_before: int, pattern: list[str]) -> bool:
    cols = min(cols_before, len(pattern[0])-cols_before)
    return all( [r[cols_before-i-1] for r in pattern] == [r[cols_before+i] for r in pattern] for i in range(cols))

def smudge_reflected_v(cols_before: int, pattern: list[str]) -> bool:
    cols = min(cols_before, len(pattern[0])-cols_before)
    return sum( sum(c1!=c2 for c1,c2 in zip((r[cols_before-i-1] for r in pattern), (r[cols_before+i] for r in pattern))) for i in range(cols))


def solve():
    with open(Path(__file__).with_name('input.txt'), 'r') as f:
        lines = f.read().split('\n')
        patterns = [[]]
        for line in lines:
            if line == '':
                patterns.append([])
            else:
                patterns[-1].append(line)
        print(f"Patterns: {patterns}")
        summary = 0
        for pattern in patterns:
            reflected_h = next((i for i in range(1,len(pattern)) if is_reflected_h(i, pattern)), None)
            reflected_v = next((i for i in range(1,len(pattern[0])) if is_reflected_v(i, pattern)), None)
            if reflected_h is not None: summary += 100 * reflected_h
            if reflected_v is not None: summary += reflected_v
            print(f"Pattern: {pattern} is reflected at V:{reflected_v} H:{reflected_h}")
        print(f"Part1: {summary}")
        summary = 0
        for pattern in patterns:
            reflected_h = next((i for i in range(1,len(pattern)) if smudge_reflected_h(i, pattern)==1), None)
            reflected_v = next((i for i in range(1,len(pattern[0])) if smudge_reflected_v(i, pattern)==1), None)
            if reflected_h is not None: summary += 100 * reflected_h
            if reflected_v is not None: summary += reflected_v
            print(f"Pattern: {pattern} is reflected at V:{reflected_v} H:{reflected_h}")
        print(f"Part2: {summary}")

if __name__ == '__main__': solve()