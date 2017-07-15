class Solution(object):
    def canJump(self, nums):
        if not nums:
            return False
        max_dist = 0
        for i in xrange(len(nums)):
            if i > max_dist:
                break
            max_dist = max(max_dist, i + nums[i])
        return max_dist >= len(nums) - 1

print Solution().canJump([3, 2, 1, 0, 4])
