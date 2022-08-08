#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashmap = {}
        for i, first_num in enumerate(nums):
            sec_num = target - first_num
            
            if sec_num in hashmap:
                return [i, hashmap[sec_num]]
            
            else:
                hashmap[first_num] = i      

# @lc code=end

