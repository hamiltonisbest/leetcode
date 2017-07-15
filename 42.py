class Solution(object):
    def trap(self, height):
        if not height:
            return 0
        n = len(height)
        left_max = [0] * n
        for i in xrange(1, n):
            left_max[i] = max(left_max[i - 1], height[i - 1])
        res = 0
        max_right = height[n - 1]
        for i in xrange(n - 2, 0, -1):
            res += max(min(left_max[i], max_right) - height[i], 0)
            max_right = max(max_right, height[i])
        return res

print Solution().trap([0])
