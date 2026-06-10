import unittest

# Valid Anagram
# Easy
# Given two strings s and t, return true if the two strings are anagrams of 
# each other, otherwise return false.

# An anagram is a string that contains the exact same characters as another 
# string, but the order of the characters can be different.

# Example 1:
# Input: s = "racecar", t = "carrace"
# Output: true

# Example 2:
# Input: s = "jar", t = "jam"
# Output: false

# Constraints:
# 1 <= s.length, t.length <= 5 * 10^4
# s and t consist of lowercase English letters.


def print_success_message(test_case) -> None:
    print(f"Unittest {test_case} passed successfuly!")


class Solution:
    # This solution has time complexity O(n + m) where n is the length of 
    # input string 1 (s) and m is the length of input string 2 (t). The
    # creation statements for the dict/hash table objects only occur once,
    # as does the final comparison statement that gives the boolean return
    # value, so those steps are complete in constant time.
    
    # The process of iteratively updating the dictionaries occurs once for
    # every letter in the two input strings.
    def is_anagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}
        for x in s:
            s_dict[x] = s_dict.get(x, 0) + 1
        for y in t:
            t_dict[y] = t_dict.get(y, 0) + 1
        
        return s_dict == t_dict


class TestSolution(unittest.TestCase):
    def test_case(
        self, s: str, t: str, expected_output: bool, test_name: str) -> None:
        
        solution = Solution()
        solution_output = solution.is_anagram(s=s, t=t)
        msg = f"Test failed for input {s}, {t}"
        self.assertEqual(
            solution_output,
            expected_output,
            msg
        )
        print_success_message(test_name)

if __name__ == "__main__":
    tests = TestSolution()
    tests.test_case('racecar', 'carrace', True, 'test_case_1')
    tests.test_case('jar', 'jam', False, 'test_case_2')