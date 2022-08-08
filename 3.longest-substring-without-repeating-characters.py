#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        sub_string = ''
        for char in s:
            if char not in sub_string:
                sub_string += char
                
            elif char in sub_string:
                if len(sub_string) >= max_length:
                    max_length = len(sub_string)
                
                sub_string = sub_string[sub_string.find(char)+1:] + char

        if len(sub_string) >= max_length:
            max_length = len(sub_string)
        

        return max_length
# @lc code=end