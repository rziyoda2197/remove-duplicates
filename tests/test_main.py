import pytest

def remove_duplicates(nums):
    seen = set()
    write_index = 0
    for read_index in range(len(nums)):
        if nums[read_index] not in seen:
            seen.add(nums[read_index])
            nums[write_index] = nums[read_index]
            write_index += 1
    return write_index

def test_remove_duplicates():
    nums = [1, 1, 2, 3, 3, 4, 5, 5]
    assert remove_duplicates(nums) == 5

def test_remove_duplicates_empty():
    nums = []
    assert remove_duplicates(nums) == 0

def test_remove_duplicates_no_duplicates():
    nums = [1, 2, 3, 4, 5]
    assert remove_duplicates(nums) == 5

def test_remove_duplicates_all_duplicates():
    nums = [1, 1, 1, 1, 1]
    assert remove_duplicates(nums) == 1
