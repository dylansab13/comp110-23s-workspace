"""EX05 - Lists + Utils."""

__author__ = "730488390"

def only_evens(one_v: list[int]) -> list[int]:
    """Returns only the even numbers in the list."""
    new_list: list[int] = list()
    for even in one_v:
        if even % 2 == 0:
            new_list.append(even)
    return new_list

def concat(one_list: list[int], two_list: list[int]) -> list[int]:
    """Returns elements of first and second string."""
    returned_list: list[int] = list()
    for numb in one_list:
        returned_list.append(numb)
    for numb in two_list:
        returned_list.append(numb)
    return returned_list

def sub(the_list: list[int], start_idx: int, end_idx: int) -> list[int]:
    """Returns a subset of the given list."""
    if len(the_list) == 0 or start_idx >= len(the_list) or end_idx <= 0:
        return []
    ending_list: list[int] = list()
    if start_idx < 0:
        start_idx = 0
    if end_idx > len(the_list):
        end_idx = len(the_list)
    for num in range(start_idx, end_idx):
        ending_list.append(the_list[num])
    return ending_list









