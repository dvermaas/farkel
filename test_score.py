from main import score

def test_straights():
    assert score((1, 2, 3, 4, 5)) == 500
    assert score((2, 3, 4, 5, 6)) == 750
    assert score((1, 2, 3, 4, 5, 6)) == 1500

def test_n_of_a_kind():
    for v in range(1, 7):
        if v == 1:
            v = 10
        for n in range(3, 7):
            print([v] * n)
            assert score((v, ) * n) == (100 * v) * (2 ** (n - 3))

def test_singles():
    for i in range(7):
        thing = 100 if i == 1 else 50 if i == 5 else 0
        assert score((i, )) == thing

def test_straight_plus():
    assert score((1, 2, 3, 4, 5, 5)) == 550
    assert score((1, 1, 2, 3, 4, 5)) == 600

def test_double_3_of_a_kind():
    assert score((1, 1, 1, 2, 2, 2)) == 1200
    assert score((1, 1, 1, 5, 5, 5)) == 1500

def test_3_of_a_kind_plus():
    assert score((1, 1, 1, 5)) == 1050
    assert score((1, 1, 1, 5, 5)) == 1100
    assert score((1, 1, 1, 5, 5, 2)) == 0