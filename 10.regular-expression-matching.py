#
# @lc app=leetcode id=10 lang=python3
#
# [10] Regular Expression Matching
#

# @lc code=start
import re

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
       p = p + '$'
       match = re.match(p, s) 
       return bool(match)
# @lc code=end

