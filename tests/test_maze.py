from src.maze import find_path

def test_simple_path():
    g = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0],
    ]
    expected = [(0,0), (1,0), (2,0), (2,1), (2,2)]
    assert find_path(g, (0,0), (2,2)) == expected

def test_blocked_start():
    g = [
        [1, 0],
        [0, 0],
    ]
    assert find_path(g, (0,0), (1,1)) is None

def test_blocked_end():
    g = [
        [0, 0],
        [0, 1],
    ]
    assert find_path(g, (0,0), (1,1)) is None

def test_no_path_maze():
    g = [
        [0, 1, 0, 0],
        [0, 1, 0, 1],
        [0, 1, 0, 1],
        [1, 0, 0, 1],  # blocked, so no path exists
    ]
    assert find_path(g, (0,0), (3,2)) is None

def test_start_equals_end():
    g = [
        [0, 1],
        [0, 0],
    ]
    assert find_path(g, (1,1), (1,1)) == [(1,1)]

def test_larger_maze():
    g = [
        [0,0,0,0,1],
        [1,1,0,1,0],
        [0,0,0,1,0],
        [0,1,1,0,0],
        [0,0,0,0,0],
    ]
    result = find_path(g, (0,0), (4,4))
    assert result[0] == (0,0)
    assert result[-1] == (4,4)
