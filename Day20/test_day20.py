from Day20.day20 import solve1

def test_day20_example1_part1():
    example = """broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a"""

    actual = solve1(example.split('\n'))

    assert actual == 32000000

def test_day20_example2_part1():
    example = """broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output"""

    actual = solve1(example.split('\n'))

    assert actual == 11687500