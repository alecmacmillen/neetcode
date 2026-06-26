import unittest
import math

# Products of Array Except Self
# Medium
# Topics: Array, Prefix Sum

# Given an integer array nums, return an array output where output[i] 
# is the product of all the elements of nums except nums[i].

# Each product is guaranteed to fit in a 32-bit integer.

# Follow-up: Could you solve it in O(n) time 
# without using the division operation?

# Example 1:
# Input: nums = [1,2,4,6]
# Output: [48,24,12,8]

# Example 2:
# Input: nums = [-1,0,1,2,3]
# Output: [0,-6,0,0,0]

# Constraints:
# 2 <= nums.length <= 1000
# -20 <= nums[i] <= 20

# Recommended Time & Space Complexity
# You should aim for a solution as good or better than O(n) time and O(n) 
# space, where n is the size of the input array.

def print_success_message(test_case):
    print(f"Unittest passed successfully for test {test_case}!")

class Solution:
    def product_except_self(self, nums: list[int]) -> list[int]:
        """
        """
        length = len(nums)
        lefts = [math.prod(nums[0:i]) if i > 0 else 1 for i in range(length)]
        rights = [math.prod(nums[i+1:length+1]) if i < length+1 else 1 for i in range(length)]
        return [lefts[i] * rights[i] for i in range(length)]
    
    def product_except_self_accepted(
        self, nums: list[int]) -> list[int]:
        """
        """
        pass

class TestSolution(unittest.TestCase):
    """
    """
    def run_test(self, nums: list[int], expected_output: list[int]):
        """
        """
        solution = Solution()
        actual_output = solution.product_except_self(nums)
        msg = f'Unittest failed for test case {nums}'
        self.assertEqual(
            actual_output,
            expected_output,
            msg
        )
        print_success_message(nums)
    
    def run_test_accepted(self, nums: list[int], expected_output: list[int]):
        """
        """
        solution = Solution()
        actual_output = solution.product_accept_self_accepted(nums)
        msg = f'Unittest failed for test case {nums}'
        self.assertEqual(
            expected_output,
            actual_output,
            msg
        )
        print_success_message(nums)


if __name__ == "__main__":
    # Define test cases
    t1_input = []
    t1_expected_output = []

    t2_input = []
    t2_expected_output = []

    test = TestSolution()
    test.run_test(t1_input, t1_expected_output)
    test.run_test(t2_input, t2_expected_output)
    test.run_test_accepted(t1_input, t1_expected_output)
    test.run_test_accepted(t2_input, t2_expected_output)