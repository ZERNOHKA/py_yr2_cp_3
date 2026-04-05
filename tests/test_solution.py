from contest.main import array_diff, sum_pairs, remove_duplicate_ids, lazy

def test_array_diff():
    """Тесты к Задаче №1"""
    assert array_diff([1,2], [1]) == [2]
    assert array_diff([1,2,2], [1]) == [2,2]
    assert array_diff([1,2,2], [2]) == [1]
    assert array_diff([1,2,2], []) == [1,2,2]
    assert array_diff([], [1,2]) == []
    assert array_diff([1,2,3], [1, 2]) == [3]
    
def test_sum_pairs():
    """Тесты к Задаче №2"""
    l1 = [1, 4, 8, 7, 3, 15]
    l2 = [1, -2, 3, 0, -6, 1]
    l3 = [20, -13, 40]
    l4 = [1, 2, 3, 4, 1, 0]
    l5 = [10, 5, 2, 3, 7, 5]
    l6 = [4, -2, 3, 3, 4]
    l7 = [0, 2, 0]
    l8 = [5, 9, 13, -3]
    l9 = [1] * 10000000
    l9[len(l9) // 2 - 1] = 6
    l9[len(l9) // 2] = 7
    l9[len(l9) - 2] = 8
    l9[len(l9) - 1] = -3
    l9[0] = 13
    l9[1] = 3
    
    assert sum_pairs(l1, 8) == [1, 7]
    assert sum_pairs(l2, -6) == [0, -6]
    assert sum_pairs(l3, -7) is None
    assert sum_pairs(l4, 2) == [1, 1]
    assert sum_pairs(l5, 10) == [3, 7]
    assert sum_pairs(l6, 8) == [4, 4]
    assert sum_pairs(l7, 0) == [0, 0]
    assert sum_pairs(l8, 10) == [13, -3]
    assert sum_pairs(l9, 13) == [6, 7]
    assert sum_pairs(l9, 5) == [8, -3]
    assert sum_pairs(l9, 16) == [13, 3]
    assert sum_pairs(l9, 31) is None
    
def test_remove_duplicate_ids():
    """Тесты к Задаче №3"""
    a = {
        "1": ["A", "B", "C"],
        "2": ["A", "B", "D", "A"],
    }
    res_a = {
        "1": ["C"],
        "2": ["A", "B", "D"]
    }
    assert remove_duplicate_ids(a) == res_a

    b = {
        "1": ["C", "F", "G"],
        "2": ["A", "B", "C"],
        "3": ["A", "B", "D"],
    }
    res_b = {
        "1": ["F", "G"],
        "2": ["C"],
        "3": ["A", "B", "D"]
    }
    assert remove_duplicate_ids(b) == res_b

    c = {
        "1": ["A"],
        "2": ["A"],
        "3": ["A"],
    }
    res_c = {
        "1": [],
        "2": [],
        "3": ["A"]
    }
    assert remove_duplicate_ids(c) == res_c

    d = {
        "432": ["A", "A", "B", "D"],
        "53": ["L", "G", "B", "C"],
        "236": ["L", "A", "X", "G", "H", "X"],
        "11": ["P", "R", "S", "D"],
    }
    res_d = {
        "11": ["P", "R", "S"],
        "53": ["C"],
        "236": ["L", "X", "G", "H"],
        "432": ["A", "B", "D"]
    }
    assert remove_duplicate_ids(d) == res_d
    
def test_lazy():
    """Тесты к Задаче №4"""
    for i in range(1, 6):
        @lazy(i)
        def mul(a, b):
            return a*b
        for j in range(3*i):
            val = None if j%i else 56
            assert mul(7, 8) == val
                
    for i in range(1, 6):
        @lazy(-i)
        def mul(a, b):
            return a*b
        for j in range(1, 3*i+ 1):
            val = 56 if j%i else None
            assert mul(7, 8) == val
    