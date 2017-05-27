class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        res = []
        for i in xrange(len(nums) - 2):
            if i == 0 or nums[i] != nums[i - 1]:
                left, right = i + 1, len(nums) - 1
                while left < right:
                    s = nums[i] + nums[left] + nums[right]
                    if s == 0:
                        res.append([nums[i], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif s < 0:
                        left += 1
                    else:
                        right -= 1
        return res

solution = Solution()
print solution.threeSum([0, 0, 0, 1, -1])
