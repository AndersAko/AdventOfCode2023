from pathlib import Path
from day18 import solve1, solve2

input = """R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)"""

def test_solve1():
    result = solve1(input.split('\n'))

    assert result == 62

def test_solve2_short():
    result = solve2(input.split('\n'), False)

    assert result == 62

def test_solve2():
    result = solve2(input.split('\n'), True)

    assert result == 952408144115

def test_solve2_part1_input():
    with open(Path(__file__).with_name('input.txt'), 'r') as f:
        lines = f.read().split('\n')
        answer = solve2(lines, False)

        assert answer == 49061