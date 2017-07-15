class Solution(object):
    def maxSubArray(self, nums):
        cur, max_sum = nums[0], nums[0]
        for x in nums[1:]:
            cur = x if cur <=0 else x + cur
            max_sum = max(max_sum, cur)
        return max_sum

print Solution().maxSubArray([-1])
