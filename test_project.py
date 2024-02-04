from project import valid_diff, nscore, order, funalg

def test_valid_diff():
    assert valid_diff("e") == True
    assert valid_diff("m") == True
    assert valid_diff("h") == True
    assert valid_diff("H") == False
    assert valid_diff("234") == False


def test_nscore():
    assert nscore('e', 4) == 5
    assert nscore('e', 1) == 2
    assert nscore('e', 60) == 0
    assert nscore('m', 60) == 0
    assert nscore('h', 60) == 0
    assert nscore('m', 4) == 14
    assert nscore('m', 2) == 8
    assert nscore('h', 1) == 3
    assert nscore('h', 4) == 18


def test_order():
    assert order(1) == 4
    assert order(2) == 1
    assert order(3) == 3
    assert order(4) == 2
    assert order(5) == 8
    assert order(6) == -5
    assert order(7) == 7
    assert order(8) == 6

def test_funalg():
    assert funalg(3, -3) == -10
    assert funalg(3, 11) == -10
    assert funalg(3, 5) == 15
    assert funalg(-5, 5) == -25
