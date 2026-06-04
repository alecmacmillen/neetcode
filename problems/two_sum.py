import unittest
import copy

# Two Sum
# Topics: array, hash table
# Recommended Time and Space Complexity:
# You should aim for a solution with O(n) time and O(n) space, 
# where n is the size of the input array.

# Given an array of integers 'nums' and an integer 'target', return the indices
# i and j such that nums[i] + nums[j] == target and i != j. You may assume 
# that every input has exactly one pair of indices i and j that satisfy the 
# condition. Return the answer with the smaller index first.

# Example 1:
# Input: 
# nums = [3,4,5,6], target = 7
# Output: [0,1]
# Explanation: nums[0] + nums[1] == 7, so we return [0, 1].

# Example 2:
# Input: nums = [4,5,6], target = 10
# Output: [0,2]

# Example 3:
# Input: nums = [5,5], target = 10
# Output: [0,1]

# Constraints:
# 2 <= nums.length <= 1000
# -10,000,000 <= nums[i] <= 10,000,000
# -10,000,000 <= target <= 10,000,000
# Only one valid answer exists.

def print_success_message(test_case) -> None:
    print(f'Unittest {test_case} passed successfully!')

class Solution:
    def two_sum_initial(self, nums: list[int], target: int) -> list[int]:
        """
        Naive approach
        1. Iterate through the array
        2. For each number, calculate a remainder by subtracting
           current number from the target
        3. If the remainder is half the target and that same number appears
           more than once in the input, return the two indices
        4. Otherwise, if the sums add up, return the indices
        5. If the sums don't add up, continue iterating
        """
        for n in nums:
            remainder = target - n
            if n == remainder and nums.count(n) > 1:
                return sorted([i for i, x in enumerate(nums) if x == n])
            elif remainder in nums:
                if n == remainder:
                    continue
                return sorted([nums.index(n), nums.index(remainder)])
    
    def two_sum_sorting(self, nums: list[int], target: int) -> list[int]:
        """
        Two sum algorithm
        1. Create a copy of the input array and sort it
           (store elements as tuple wih value and index)
        2. Create two pointers: one at end of array and one at beginning
        3. Iterate through array: add the elements at each pointer location
        4. If equal to target, return indexes from the tuples
        5. If smaller, move the left pointer (i) up one (+1 to right)
        6. If larger, move the right pointer (j) back one (-1 to left)
        7. Repeat until solution found

        Time complexity: O(n*lg(n))
        """
        A = []
        for i, num in enumerate(nums):
            A.append([num, i])
        A.sort()

        i, j = 0, len(nums) - 1
        while i < j:
            cur = A[i][0] + A[j][0]
            if cur == target:
                return [min(A[i][1], A[j][1]),
                        max(A[i][1], A[j][1])]
            elif cur < target:
                i += 1
            else:
                j -= 1
        return []
    
    def two_sum_hash_map(self, nums: list[int], target: int) -> list[int]:
        """
        1. Create a dict/hash map to store keys in
        2. Iterate through the input array 'nums'
        3. For each value, find its complement by subtracting from target
        4. If complement exists in the hash map, return indices
        5. If complement does not exist in hash map, add it where value from
         nums is the hash map key and the index in nums input is hash map value
        6. Continue iterating until solution is found

        Complexity:
            Time = O(n) --> iterates once through the nums array so number
                of steps is proportional to length of the nums array
            Space = O(n) --> creates a dict/hash map that has in worst case
                same number of keys as length of input array (n)
        """
        hash_map = {}
        for i, num in enumerate(nums):
            comp = target - num
            if comp in hash_map:
                return sorted([hash_map[comp], i])
            else:
                hash_map[num] = i
        return []


class TestSolution(unittest.TestCase):
    """
    """
    def test_case(
        self, nums: list[int], target: int, expected_output: list[int]):

        solution = Solution()
        solution_output = solution.two_sum_hash_map(nums, target)
        msg = f'Test failed for input {nums}, {target}. Expected {expected_output}, got {solution_output}'
        self.assertEqual(
            solution_output,
            expected_output,
            msg
        )
        print_success_message(str(nums))

if __name__ == "__main__":
    tests = TestSolution()
    tests.test_case(nums=[3, 4, 5, 6], target=7, expected_output=[0, 1])
    tests.test_case(nums=[4, 5, 6], target=10, expected_output=[0, 2])
    tests.test_case(nums=[1, 3, 5, 7], target=12, expected_output=[2, 3])
    tests.test_case(nums=[5,5], target=10, expected_output=[0, 1])
    tests.test_case(nums=[1, 3, 4, 2], target=6, expected_output=[2, 3])