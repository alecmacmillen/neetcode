import unittest
# Top K Frequent Elements
# Medium

# Given an integer array nums and an integer k, return the k most frequent 
# elements within the array. The test cases are generated such that the answer
# is always unique. You may return the output in any order.

# Example 1:
# Input: nums = [1,2,2,3,3,3], k = 2
# Output: [2,3]

# Example 2:
# Input: nums = [7,7], k = 1
# Output: [7]

# Constraints:
# 1 <= nums.length <= 10^4.
# -1000 <= nums[i] <= 1000
# 1 <= k <= number of distinct elements in nums.

# Topics
# Array, hash table, divide and conquer, sorting, heap (priority queues),
# bucket sort, counting, quickselect

# Recommended Time & Space Complexity
# You should aim for a solution with O(n) time and O(n) space, where n is the size of the input array.
def print_success_message(test_case) -> None:
    print(f'Unittest {test_case} passed successfully!')


class Solution:
    def naive_top_k_frequent(self, nums: list[int], k: int) -> list[int]:
        """
        OK so my first naive thought is to iterate through the list
        and populate a dictionary where the key is the number and
        the value is the number of times it appears, then put
        the key-val pairs in a list, sort it, and select the last k items

        This is what neetcode calls the "Naive" solution: O(n*lg(n)) time
        because of the sorting step - remember sorted() uses timesort, which
        is n * lg(n)

        This solution does work, however.
        """
        counts = {}
        for n in nums:
            counts[n] = counts.get(n, 0) + 1
        sorted_list = sorted(list(counts.items()), key=lambda x: x[1])
        return [x[0] for x in sorted_list[-k:]]
    
    def top_k_frequent(self, nums: list[int], k: int) -> list[int]:
        """
        Use the BUCKET SORT algorithm to create n buckets, grouping
        numbers based on their frequencies from 1 to n. Then, pick
        the top k numbers from the buckets, starting from n down to 1
        """
        # Both of these objects are O(n) space; the size of the buckets
        # array is only 1 more than the size of the list and the size
        # of the counts dict/hash table is at most the same size as the
        # number of items in the input list. O(n) + O(n) = constant time
        # Can't just do [ [] ] * len(nums) because that creates shallow
        # copies of empty lists that all reference the same object and
        # any update to one list will update them all
        buckets = [ [] for i in range(len(nums) + 1) ] 
        counts = {}

        # This loop is O(n) --> iterate through each item in the list 1x
        for n in nums:
            counts[n] = counts.get(n, 0) + 1
        
        # This loop is also O(n) --> 
        for key, val in counts.items():
            buckets[val].append(key)
        
        # Create an empty list to store results in
        result = []
        # This loop is O(n): iterate through 'buckets' list of list 
        # 1 element at a time, where the index is the frequency and
        # the list elements of the nested sublist are the values from
        # the original input
        for i in range(len(buckets) - 1, 0, -1):
            # This loop is also O(n): iterate through the sublists
            # which in worst case would be length n (if the input list
            # had all the same value over and over))
            for n in buckets[i]:
                result.append(n)
                # Once you have a result with the same length as desired
                # k, terminate
                if len(result) == k:
                    return result
        
        # Big takeaway: as long as you only have loops that take O(n)
        # time, you can have as many as you want and they compose into
        # constant time


class TestSolution(unittest.TestCase):
    def test_case(
        self, nums: list[int], k: int, expected_output: list[int]):

        solution = Solution()
        sres, iolution_output = solution.top_k_frequent(nums, k)
        msg = f"""Test failed for input {nums}, {k}. Expected
            {expected_output}, got {solution_output}."""
        # Use assertCountEqual() because we just want to be sure the 
        # elements of the list are the same, we don't care about order
        self.assertCountEqual(solution_output, expected_output, msg)
        print_success_message(str(nums))


if __name__ == "__main__":
    tests = TestSolution()
    tests.test_case(nums=[1,2,2,3,3,3], k=2, expected_output=[2,3])
    tests.test_case(nums=[7,7], k=1, expected_output=[7])