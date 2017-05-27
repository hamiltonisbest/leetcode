class Solution(object):
    def firstMissingPositive(self, nums):
        if not nums:
            return 1
        n = len(nums)
        for i in xrange(n):
            j = nums[i]
            while j != i + 1 and j > 0 and j <= n and j != nums[j - 1]:
                nums[i], nums[j - 1] = nums[j - 1], nums[i]
                j = nums[i]
        for i in xrange(n):
            if i + 1 != nums[i]:
                return i + 1
        return n + 1

print Solution().firstMissingPositive([5, 1, 2, 3])
