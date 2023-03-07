"""EX05 - Lists + Utils Unit Tests."""

__author__ = "730488390"

from exercises.ex05.utils import only_evens, concat, sub

def test_only_evens_use() -> None:
    """Tests the function returning only even numbers"""
    assert only_evens([1, 2, 3]) == [2]

def test_only_evens_use_two() -> None:
    """Returns the function as an empty list because all are odd"""
    assert only_evens([1, 3, 5]) == []

def test_only_evens_edge() -> None:
    """Returns the function as empty"""
    assert only_evens([]) == []



def test_concat_use() -> None:
    """Tests the function combining both lists"""
    assert concat([1,2], [3,4]) == [1,2,3,4]

def test_concat_use_two() -> None:
    """Tests the function combining one list"""
    assert concat([1,2], []) == [1,2,3,4]

def test_concat_edge() -> None:
    """Tests function with empty list"""
    assert concat([], "") == ""



def test_sub_use_one() -> None:
    """Tests the function with correct index numbers"""
    assert sub([10,20,30,40], 1, 3) == [20,30]

def test_sub_use_two() -> None:
    """Tests function with invalid index numbers"""
    assert sub("Hello, world!", 7, 18) == "world!"

def test_sub_edge() -> None:
    """Tests function with empty string"""
    assert sub([], 0, 3) == []

if __name__ == "__main__":
    test_only_evens_edge()
    test_only_evens_use()
    test_concat_use_two()
    test_concat_edge()
    test_concat_use()
    test_concat_use_two()
    test_sub_edge
    test_sub_use_one
    test_sub_use_two

