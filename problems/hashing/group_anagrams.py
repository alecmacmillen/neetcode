import unittest
from collections import defaultdict

# Group Anagrams
# Medium
# Topics: Array, Hash Table, String, Sorting

# Given an array of strings strs, group all anagrams together into sublists. 
# You may return the output in any order. An anagram is a string that contains 
# the exact same characters as another string, but the order of the characters 
# can be different.

# Example 1:
# Input: strs = ["act","pots","tops","cat","stop","hat"]
# Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

# Example 2:
# Input: strs = ["x"]
# Output: [["x"]]

# Example 3:
# Input: strs = [""]
# Output: [[""]]
# Constraints:

# 1 <= strs.length <= 1000.
# 0 <= strs[i].length <= 100
# strs[i] is made up of lowercase English letters.

# Recommended Time & Space Complexity
# You should aim for a solution with O(m * n) time and O(m) space, 
# where m is the number of strings and n is the length of the longest string.

def print_success_message(test_case):
    print(f"Unittest passed successfully for test {test_case}!")


class Solution:
    def group_anagrams(self, strs: list[str]) -> list[list[str]]:
        """
        1. Create hash table to store template strings
        2. Iterate through input list
        3. For each string, sort it alphabetically and check if it's in 
            the hash_table.
        4. The value of each template string key is a list of all words
            that belong to that template.
        5. Once the list has been iterated through, return the values
            from the hash table as a list of lists

        Time complexity: for-loop executes once for every 'm' element in the
            input list. Each iteration takes n * lg(n) time, where n is the
            length of the word, because the sorted() method uses timesort,
            which is a comparison-based sorting algorithm that runs in
            n * lg(n) time.
        
        Space complexity: creates a hash table object that has at most 'm'
            keys (if there are no anagrams and all strings in input have
            distinct character composition) - O(m) space complexity
        """
        hash_table = {}
        for s in strs:
            x = "".join(sorted(s))
            if x not in hash_table.keys():
                hash_table[x] = [s]
            else:
                hash_table[x].append(s)
        return list(hash_table.values())
    
    def group_anagrams_accepted(self, strs: list[str]) -> list[list[str]]:
        """
        1. Create a hash table using the defaultdict which
            automatically makes all keys lists
        2. Iterate through each string in the input
        3. Create a mutable list of 26 0's to store the counts of
            each character in the alphabet
        4. Convert a = 0, b = 1, ..., z = 26 by taking advantage of
            the ord() "ordinal" function and subtracting the value of
            "a", which is 80. So a = 80 - 80 = 0, b = 81 - 80 = 1, etc.
        5. Lists are mutable so they cannot be hash table keys, so
            convert them to non-mutable tuples.
        6. Add the word being analyzed to the list value for the 
            corresponding count tuple
        
        This run has time complexity O(m * n) because we're not sorting 
        the strings before adding them to the hash table, we're simply
        iterating through them to create the char_count tuple that we use
        as a hash table key. Iterating through a string of length 'n'
        has time complexity n as opposed to sorting it in our last example,
        which had time complexity n * lg(n).
        """
        hash_table = defaultdict(list)
        for s in strs:
            char_count = [0] * 26
            for c in s:
                char_count[ord(c) - ord("a")] += 1
            hash_table[tuple(char_count)].append(s)
        return list(hash_table.values())


class TestSolution(unittest.TestCase):
    """
    """
    def run_test(self, strs_input: list[str], 
        expected_output: list[list[str]], test_case_name) -> None:

        solution = Solution()
        actual_output = solution.group_anagrams(strs_input)
        for x, y in zip(actual_output, expected_output):
            x.sort()
            y.sort()

        msg = f'Self-solution unittest failed for test input {strs_input}'
        self.assertEqual(
            sorted(expected_output),
            sorted(actual_output),
            msg
        )
        print_success_message(test_case_name)
    
    def run_test_accepted(self, strs_input: list[str], 
        expected_output: list[list[str]], test_case_name) -> None:

        solution = Solution()
        actual_output = solution.group_anagrams_accepted(strs_input)
        for x, y in zip(actual_output, expected_output):
            x.sort()
            y.sort()

        msg = f'Accepted solution unittest failed for test input {strs_input}'
        self.assertEqual(
            sorted(expected_output),
            sorted(actual_output),
            msg
        )
        print_success_message(test_case_name)


if __name__ == "__main__":
    # Define test cases
    t1_input = ["act", "pots", "tops", "cat", "stop", "hat"]
    t1_expected_output = [
        ["hat"], ["act", "cat"], ["stop", "pots", "tops"]]
    t2_input = ["x"]
    t2_expected_output = [["x"]]
    t3_input = [""]
    t3_expected_output = [[""]]
    t4_input = ["eat", "tea", "tan", "ate", "nat", "bat"]
    t4_expected_output = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
    
    test = TestSolution()
    # Run tests for self-solution
    test.run_test(t1_input, t1_expected_output, "t1")
    test.run_test(t2_input, t2_expected_output, "t2")
    test.run_test(t3_input, t3_expected_output, "t3")
    test.run_test(t4_input, t4_expected_output, "t4")
    # Run tests for expected solution
    test.run_test_accepted(t1_input, t1_expected_output, "t1")
    test.run_test_accepted(t2_input, t2_expected_output, "t2")
    test.run_test_accepted(t3_input, t3_expected_output, "t3")
    test.run_test_accepted(t4_input, t4_expected_output, "t4")