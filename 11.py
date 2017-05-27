class Solution(object):
    def maxArea(self, height):
        if not height or len(height) <= 1:
            return 0
        n = len(height)
        max_area = 0
        left, right = 0, n - 1
        while left < right:
            max_area = max(max_area, (right - left) * min(height[left], height[right]))
            if height[left] < height[right]:
                k = left
                while k < right and height[k] <= height[left]:
                    k += 1
                left = k
            else:
                k = right
                while k > left and height[k] <= height[right]:
                    k -= 1
                right = k
        return max_area

print Solution().maxArea([1, 2, 3, 4])
