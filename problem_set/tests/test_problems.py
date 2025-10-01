import pytest
from problem_set import solutions as s


def test_sum_of_even():
    assert s.sum_of_even(0) == 0
    assert s.sum_of_even(1) == 0
    assert s.sum_of_even(2) == 2
    assert s.sum_of_even(10) == 30


def test_is_anagram():
    assert s.is_anagram('Listen', 'Silent')
    assert s.is_anagram('Dormitory', 'Dirty room!!')
    assert not s.is_anagram('abc', 'ab')


def test_fibonacci():
    assert s.fibonacci(0) == 0
    assert s.fibonacci(1) == 1
    assert s.fibonacci(10) == 55
    with pytest.raises(ValueError):
        s.fibonacci(-1)


def test_flatten():
    assert s.flatten([]) == []
    assert s.flatten([1, [2, [3, 4], 5], 6]) == [1, 2, 3, 4, 5, 6]


def test_group_by_key():
    items = [{'a': 1, 'x': 10}, {'a': 2}, {'a': 1}, {'b': 5}]
    grouped = s.group_by_key(items, 'a')
    assert grouped[1] == [{'a': 1, 'x': 10}, {'a': 1}]
    assert grouped[2] == [{'a': 2}]
    assert grouped[None] == [{'b': 5}]


def test_shortest_path():
    grid1 = [[0, 0, 0], [1, 1, 0], [0, 0, 0]]
    assert s.shortest_path(grid1) == 4
    grid2 = [[0, 1], [1, 0]]
    assert s.shortest_path(grid2) == -1
    grid3 = [[0]]
    assert s.shortest_path(grid3) == 0
