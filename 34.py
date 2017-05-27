class Solution(object):
    def searchRange(self, nums, target):
        if not nums or target < nums[0] or target > nums[-1]:
            return [-1, -1]
        return [Solution.search(self, nums, target, -1), Solution.search(self, nums, target, 1)]

    def search(self, nums, target, direction):
        left, right = 0, len(nums) - 1
        res = -1
        while left <= right:
            mid = (left + right) >> 1
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                res = mid
                if direction == -1:
                    right = mid - 1
                else:
                    left = mid + 1
        return res

#print Solution().searchRange([1, 2, 2, 3], 2)
print Solution().searchRange([5, 7, 7, 8, 8, 10], 8)
