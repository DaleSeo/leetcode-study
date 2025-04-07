class Solution:
    def rob(self, nums):
        num_map = {}
        for i, num in enumerate(nums):
            left = num_map.get(i - 2, 0)
            leftleft = num_map.get(i - 3, 0)
            num_map[i] = max(left + num, leftleft + num)  
        return max(num_map.get(len(nums) - 1, 0), num_map.get(len(nums) - 2, 0))

