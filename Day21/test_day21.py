from day21 import solve1

input = """...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
...........""".split('\n')

def test_solve1():
    actual = solve1(input, 6)

    assert actual == 16