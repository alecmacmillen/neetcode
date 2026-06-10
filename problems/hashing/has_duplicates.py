import unittest

# Contains Duplicate
# Easy
# Given an integer array nums, return true if any value appears more than once
# in the array, otherwise return false.

# Example 1:
# Input: nums = [1, 2, 3, 3]
# Output: true

# Example 2:
# Input: nums = [1, 2, 3, 4]
# Output: false

# Recommended Time & Space Complexity
# You should aim for a solution with O(n) time and O(n) space, 
# where n is the size of the input array.

# Topics: Array, Hash Table, Sorting


def print_success_message(test_case) -> None:
    print(f"Unittest {test_case} passed successfully!")

class Solution:
    # This solution has time complexity O(n), because in the worst case it
    # will iterate through the entire "nums" list (which is itself length
    # n) one time. If the num object does not exist in the counts set,
    # it is added. If it does exist, that number has been seen before, so
    # the function immediately terminates and evaluates to True.

    # It has space complexity O(n), because it creates a set that in the
    # worst case will end up being the same size as the input list.

    ### FURTHER WORK: implement a Python set from scratch using a hash set
    def hasDuplicate(self, nums: list[int]) -> bool:
        counts = set()
        for num in nums:
            if num in counts:
                return True
            else:
                counts.add(num)
        return False


class TestSolution(unittest.TestCase):
    def test_case_1(self) -> None:
        test_input = [1, 2, 3, 3]
        solution = Solution()
        solution_output = solution.hasDuplicate(test_input)
        msg = f"Test failed for input {test_input}."
        
        self.assertEqual(
            solution_output,
            True,
            msg
        )
        print_success_message("test_case_1")
    
    def test_case_2(self) -> None:
        test_input = [1, 2, 3, 4]
        solution = Solution()
        solution_output = solution.hasDuplicate(test_input)
        msg = f"Test failed for input {test_input}."

        self.assertEqual(
            solution_output,
            False,
            msg
        )
        print_success_message("test_case_2")


if __name__ == "__main__":
    tests = TestSolution()
    tests.test_case_1()
    tests.test_case_2()