class Solution(object):
    def jump(self, nums):
        if not nums:
            return 0
        cur, max_dist, res = 0, 0, 0
        for i, x in enumerate(nums):
            if cur < i:
                res += 1
                cur = max_dist
            max_dist = max(max_dist, x + i)
        return res

print Solution().jump([2, 3, 1, 1, 4])
