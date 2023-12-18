from day17 import ultra_moves, Move, Dir

def test_part2_min_4_max_10_from_start_horiz():
    cost_map = ["1111111111111", "2222222222222"]
    expected = [2,1,1,1,2,2,2,2,2,1]
    move = Move(0,0,1,None,0,[(0,0)])
    for i in range(9):
        new_moves = ultra_moves(move, cost_map)
        assert len(new_moves) == expected[i]
        move, = (m for m in new_moves if m.dir == Dir.East)
    new_moves = ultra_moves(move, cost_map)
    assert next(m.dir == Dir.South for m in new_moves)
    assert len(new_moves) == 1

def test_part2_min_4_max_10_from_start_vert():
    cost_map = ["1111111111111", "2222222222222", "1111111111111", "2222222222222", "1111111111111", "2222222222222", "1111111111111", "2222222222222", "1111111111111", "2222222222222", "1111111111111", "2222222222222"]
    expected = [2,1,1,1,2,2,2,2,2,1]
    move = Move(0,0,1,None,0,[(0,0)])
    for i in range(9):
        new_moves = ultra_moves(move, cost_map)
        assert len(new_moves) == expected[i]
        move, = (m for m in new_moves if m.dir == Dir.South)
    new_moves = ultra_moves(move, cost_map)
    assert next(m.dir == Dir.East for m in new_moves)
    assert len(new_moves) == 1


def test_part2_min_4_max_10_middle_horiz():
    cost_map = ["1111111111111", "2222222222222", "1111111111111", "2222222222222", "1111111111111", "2222222222222", "1111111111111", "2222222222222", "1111111111111", "2222222222222", "1111111111111", "2222222222222"]
    expected = [2,1,1,1,3,3,3,3,3,1]
    move = Move(0,0,1,None,0,[(0,0)])
    for i in range(5):
        new_moves = ultra_moves(move, cost_map)
        move, = (m for m in new_moves if m.dir == Dir.South)

    for i in range(9):
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
    expected = [2,1,1,1,3,3,3,3,3,1]
    move = Move(0,0,1,None,0,[(0,0)])
    for i in range(5):
        new_moves = ultra_moves(move, cost_map)
        move, = (m for m in new_moves if m.dir == Dir.East)

    for i in range(9):
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

def test_part_1
