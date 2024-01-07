import pytest
from Day23.day23 import single_route, solve1, solve2

@pytest.fixture
def aoc_map():
    return """#.#####################
#.......#########...###
#######.#########.#.###
###.....#.>.>.###.#.###
###v#####.#v#.###.#.###
###.>...#.#.#.....#...#
###v###.#.#.#########.#
###...#.#.#.......#...#
#####.#.#.#######.#.###
#.....#.#.#.......#...#
#.#####.#.#.#########v#
#.#...#...#...###...>.#
#.#.#v#######v###.###v#
#...#.>.#...>.>.#.###.#
#####v#.#.###v#.#.###.#
#.....#...#...#.#.#...#
#.#########.###.#.#.###
#...###...#...#...#.###
###.###.#.###v#####v###
#...#...#.#.>.>.#.>.###
#.###.###.#.###.#.#v###
#.....###...###...#...#
#####################.#""".split('\n')
 
def test_day23_part1(aoc_map):
    actual = solve1(aoc_map)

    assert actual == 94

def test_single_route_start(aoc_map):
    routes = dict()
    actual = single_route((0, 1), (-1,0), routes, aoc_map)
    assert actual is not None
    dest, coming_from, route_len = actual

    assert dest == (5, 3)
    assert route_len == 15
    assert coming_from == (4,3)

def test_single_route_from_cross_road(aoc_map):
    routes = dict()
    actual = single_route((5, 3), (4,3), routes, aoc_map)
    assert actual is None

def test_single_route_mid(aoc_map):
    routes = dict()
    actual = single_route((5, 4), (5,3), routes, aoc_map)
    assert actual is not None
    dest, coming_from, route_len = actual

    assert dest == (3, 11)
    assert route_len == 21
    assert coming_from == (3,10)

def test_single_route_end(aoc_map):
    routes = dict()
    actual = single_route((20, 19), (19,19), routes, aoc_map)
    assert actual is not None
    dest, coming_from, route_len = actual

    assert dest == (22, 21)
    assert route_len == 4
    assert coming_from == (21,21)


def test_day23_part2(aoc_map):

    actual = solve2(aoc_map)

    assert actual == 154
