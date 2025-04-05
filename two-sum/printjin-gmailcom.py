class Solution:
    def twoSum(self, nums, target):
        num_map = {}
        for i, num in enumerate(nums):
            left = target - num
            if left in num_map:
                return [num_map[left], i]
            num_map[num] = i  

