from day15 import hash, run_step, solve1, solve2

def test_hash():
    input = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"
    expected = [30,253,97,47,14,180,9,197,48,214,231]

    for i,s in enumerate(input.split(',')):
        h=hash(s)
        assert h == expected[i]

def test_solve1():
    input = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"
    expected = [30,253,97,47,14,180,9,197,48,214,231]

    actual = solve1(input)

    assert actual == 1320

def test_run_step():
    input = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"
    expected = [{0: [('rn',1)]},
                {0: [('rn',1)]},
                {0: [('rn',1)], 1: [('qp',3)]},
                {0: [('rn',1), ('cm',2)], 1: [('qp',3)]},
                {0: [('rn',1), ('cm',2)]},
                {0: [('rn',1), ('cm',2)], 3: [('pc',4)]},
                {0: [('rn',1), ('cm',2)], 3: [('pc',4),('ot',9)]},
                {0: [('rn',1), ('cm',2)], 3: [('pc',4),('ot',9),('ab',5)]},
                {0: [('rn',1), ('cm',2)], 3: [('ot',9),('ab',5)]},
                {0: [('rn',1), ('cm',2)], 3: [('ot',9),('ab',5),('pc',6)]},
                {0: [('rn',1), ('cm',2)], 3: [('ot',7),('ab',5),('pc',6)]},
                ]
    boxes = dict()

    for i, step in enumerate(input.split(',')):
        boxes = run_step(step, boxes)
        assert {n:b for n,b in boxes.items() if b != []} == expected[i]

def test_solve2():
    input = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"
    answer = solve2(input)

    assert answer == 145