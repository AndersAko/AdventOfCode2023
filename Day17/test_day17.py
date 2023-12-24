from day17 import ultra_moves, Move, Dir, part1, part2

def test_part2_min_4_max_10_from_start_horiz():
    cost_map = ["1111111111111", "2222222222222"]
    expected = [2,1,1,1,2,2,2,2,2,2,1]
    move = Move(0,0,0,None,0,[(0,0)])
    for i in range(10):
        new_moves = ultra_moves(move, cost_map)
        assert len(new_moves) == expected[i]
        move, = (m for m in new_moves if m.dir == Dir.East)
    new_moves = ultra_moves(move, cost_map)
    assert next(m.dir == Dir.South for m in new_moves)
    assert len(new_moves) == 1

def test_part2_min_4_max_10_from_start_vert():
    cost_map = ["1111111111111", "2222222222222", "1111111111111", "2222222222222", "1111111111111", "2222222222222", "1111111111111", "2222222222222", "1111111111111", "2222222222222", "1111111111111", "2222222222222"]
    expected = [2,1,1,1,2,2,2,2,2,2,1]
    move = Move(0,0,0,None,0,[(0,0)])
    for i in range(10):
        new_moves = ultra_moves(move, cost_map)
        assert len(new_moves) == expected[i]
        move, = (m for m in new_moves if m.dir == Dir.South)
    new_moves = ultra_moves(move, cost_map)
    assert next(m.dir == Dir.East for m in new_moves)
    assert len(new_moves) == 1


def test_part2_min_4_max_10_middle_horiz():
    cost_map = ["1111111111111", "2222222222222", "1111111111111", "2222222222222", "1111111111111", "2222222222222", "1111111111111", "2222222222222", "1111111111111", "2222222222222", "1111111111111", "2222222222222"]
    expected = [2,1,1,1,3,3,3,3,3,3,1]
    move = Move(0,0,1,None,0,[(0,0)])
    for i in range(5):
        new_moves = ultra_moves(move, cost_map)
        move, = (m for m in new_moves if m.dir == Dir.South)

    for i in range(10):
        new_moves = ultra_moves(move, cost_map)
        assert len(new_moves) == expected[i]
        if expected[i] == 3:
            assert any(m.dir == Dir.North for m in new_moves)
            assert any(m.dir == Dir.South for m in new_moves)
        move, = (m for m in new_moves if m.dir == Dir.East)
    new_moves = ultra_moves(move, cost_map)
    assert any(m.dir == Dir.North for m in new_moves)
    assert any(m.dir == Dir.South for m in new_moves)
    assert len(new_moves) == 2

def test_part2_min_4_max_10_middle_vert():
    cost_map = ["1111111111111", "2222222222222", "1111111111111", "2222222222222", "1111111111111", "2222222222222", "1111111111111", "2222222222222", "1111111111111", "2222222222222", "1111111111111", "2222222222222"]
    expected = [2,1,1,1,3,3,3,3,3,3,1]
    move = Move(0,0,1,None,0,[(0,0)])
    for i in range(5):
        new_moves = ultra_moves(move, cost_map)
        move, = (m for m in new_moves if m.dir == Dir.East)

    for i in range(10):
        new_moves = ultra_moves(move, cost_map)
        assert len(new_moves) == expected[i]
        if expected[i] == 3:
            assert any(m.dir == Dir.East for m in new_moves)
            assert any(m.dir == Dir.West for m in new_moves)
        move, = (m for m in new_moves if m.dir == Dir.South)
    new_moves = ultra_moves(move, cost_map)
    assert any(m.dir == Dir.West for m in new_moves)
    assert any(m.dir == Dir.East for m in new_moves)
    assert len(new_moves) == 2

def test_part2_maximum_10_end():
    pass

def test_part_1():
    cost_map = ["2413432311323","3215453535623","3255245654254","3446585845452","4546657867536","1438598798454","4457876987766",
                "3637877979653","4654967986887","4564679986453","1224686865563","2546548887735","4322674655533"]
    actual = part1(cost_map)
    assert actual.cost == 102

def test_part_2():
    cost_map = ["2413432311323","3215453535623","3255245654254","3446585845452","4546657867536","1438598798454","4457876987766",
                "3637877979653","4654967986887","4564679986453","1224686865563","2546548887735","4322674655533"]
    actual = part2(cost_map)
    assert actual.cost == 94

def test_part_2_special():
    cost_map = ["111111111111","999999999991","999999999991","999999999991","999999999991"]
    actual = part2(cost_map)
    assert actual.cost == 71

