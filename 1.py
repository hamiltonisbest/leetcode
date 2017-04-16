class Solution(object):
    def twoSum(self, nums, target):
        d = {}
        for i, x in enumerate(nums):
            if target - x in d:
                return [d.get(target - x), i]
            else:
                d[x] = i

#solution = Solution()
#ans = solution.twoSum([1, 2, 3], 3)
#print ans
