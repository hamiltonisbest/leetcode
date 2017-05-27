class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        res, min_dist = 0, (1 << 31) - 1
        for i in xrange(len(nums) - 2):
            if i == 0 or nums[i] != nums[i - 1]:
                left, right = i + 1, len(nums) - 1
                while left < right:
                    s = nums[i] + nums[left] + nums[right]
                    if s == target:
                        return s
                    elif s < target:
                        if target - s < min_dist:
                            min_dist = target - s
                            res = s
                        left += 1
                    else:
                        if s - target < min_dist:
                            min_dist = s - target
                            res = s
                        right -= 1
        return res

solution = Solution()
print solution.threeSumClosest([0, 0, 0, 1, -1], 0)
