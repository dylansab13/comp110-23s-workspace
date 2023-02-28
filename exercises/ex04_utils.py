"""EX04 - Utils"""

__author__ = "730488390"

def all(int_list: list[int], all_int: int) -> bool:
    "If all numbers in list are same, return True"
    num_idx: int = 0
    if len(int_list) == 0:
        return False

    while num_idx < len(int_list):
        if int_list[num_idx] != all_int:
            return False
        num_idx += 1
    return True

def max(list_ints: list[int]) -> int:
    "Figuring out the max in the list"
    if len(list_ints) == 0:
        raise ValueError(" max() arg is an empty List") 
    
    idx_numb: int = 0
    first_max: int = -2
    
    while idx_numb < len(list_ints):
        if list_ints[idx_numb] > first_max:
            first_max = list_ints[idx_numb]
        idx_numb += 1
    return first_max


def is_equal(first_list: list[int], sec_list: list[int]) -> bool:
    "Test to see if every element at every index matches"
    if len(first_list) == len(sec_list):
        test_idx: int = 0
        while test_idx < len(first_list):
            if first_list[test_idx] != sec_list[test_idx]:
                return False
            test_idx += 1
        return True
    else: 
        return False



    

 









        
