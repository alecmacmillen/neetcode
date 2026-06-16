# Encode and Decode Strings
# Medium
# Design an algorithm to encode a list of strings to a string. The encoded 
# string is then sent over the network and is decoded back to the original 
# list of strings.

# Machine 1 (sender) has the function:
# String encode(List<String> strs) {
#     // ... your code
#     return encoded_string;
# }
# Machine 2 (receiver) has the function:
# List<String> decode(String encoded_string) {
#     // ... your code
#     return decoded_strs;
# }

# So Machine 1 does:
# String encoded_string = encode(strs);

# and Machine 2 does:
# List<String> decoded_strs = decode(encoded_string);

# decoded_strs in Machine 2 should be the same as the input strs in Machine 1.

# Implement the encode and decode methods.

# Example 1:
# Input: strs = ["Hello","World"]
# Output: ["Hello","World"]
# Explanation:
# Solution solution = new Solution();
# String encoded_string = solution.encode(strs);

# Constraints:
# 0 <= strs.length < 100
# 0 <= strs[i].length < 200
# strs[i] contains any possible characters out of 256 valid ASCII characters.

# Follow up: Could you write a generalized algorithm to work on any possible 
# set of characters?

# Topics
# Recommended Time & Space Complexity
# You should aim for a solution with O(m) time for each encode() and decode() 
# call and O(m+n) space, where m is the sum of lengths of all the strings and 
# n is the number of strings.

import unittest

def print_success_message(test_case) -> None:
    print(f"Unittest {test_case} passed successfully!")


class Solution:
    def encode(self, strs: list[str]) -> str:
        encoded_str = ""
        # Result would be "5#hello5#world"
        for s in strs:
            encoded_str += str(len(s)) + "#" + s
        return encoded_str
    
    def decode(self, s: str) -> list[str]:
        decoded_str, i = [], 0
        # As long as i is in bounds for the length of s:
        while i < len(s):
            # set j equal to i: start at same index
            j = i
            while s[j] != "#":
                j += 1
            # Once you encounter a # character, convert
            # the substring from i to j to an int, this
            # is the length of the next word
            length = int(s[i:j])
            # Move pointer over from # character to first
            # letter of word and slice into the encoded string
            # using the calculated length to find the word itself
            decoded_str.append(s[j + 1 : j + 1 + length])
            # Update pointer location to 1 character after the
            # end of the word you just appended. This would be
            # the starting index for the next length substring
            i = j + 1 + length
        return decoded_str
        
    
    def encode_naive(self, strs: list[str]) -> str:
        if not strs:
            return ''
        lengths = "#".join([str(len(s)) for s in strs])
        joined_strings = "".join(strs)
        return lengths + "~" + joined_strings
    
    def decode_naive(self, s: str) -> list[str]:
        # If empty string, return empty list
        if not s:
            return []
        
        # Split the encoded string into 
        # This solution depends on the character "~" not being
        # found in any strings
        n = ""
        nums = []
        idx, strings = s.split("~")
        
        for i, x in enumerate(idx):
            # If the character being checked is not delimiter,
            # add it to the character showing how long a string is  
            if x != "#":
                n += x
            # otherwise convert it to an int and add it to indexes list
            else:
                nums.append(int(n))
                n = ""
        nums.append(int(n))

        # Initialize pointer and list to store decoded strings in
        pointer = 0
        strs = []
        for n in nums:
            # Read from the pointer position to the correct ending index
            # for each word and then update the pointer
            strs.append(strings[pointer:pointer+n])
            pointer += n
        return strs


class TestSolution(unittest.TestCase):
    def test(self, strs: list[str]) -> None:
        solution = Solution()
        encoded_str = solution.encode(strs)
        decoded_str = solution.decode(encoded_str)
        msg = f"""Encode test failed for input {strs}. Encoded and decoded
            strs do not match."""
        self.assertEqual(strs, decoded_str, msg)
        print_success_message(strs)


if __name__ == "__main__":
    tests = TestSolution()
    str1 = ["Hello", "world"]
    tests.test(str1)

    str2 = []
    tests.test(str2)

    str3 = [""]
    tests.test(str3)

# Neetcode results
# Runtime: 29ms; beats 99.90%
# Memory: 8mb; beats 99.00%