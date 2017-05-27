class Solution(object):
    def findKth(self, nums1, len1, nums2, len2, k):
        if len1 > len2:
            return Solution.findKth(self, nums2, len2, nums1, len1, k)
        if len1 == 0:
            return nums2[k - 1]
        if k == 1:
            return min(nums1[0], nums2[0])
        pa = min(k / 2, len1)
        pb = k - pa
        if nums1[pa - 1] < nums2[pb - 1]:
            return Solution.findKth(self, nums1[pa:], len1 - pa, nums2, len2, k - pa)
        elif nums1[pa - 1] > nums2[pb - 1]:
            return Solution.findKth(self, nums1, len1, nums2[pb:], len2 - pb, k - pb)
        else:
            return nums1[pa - 1]

    def findMedianSortedArrays(self, nums1, nums2):
        len1, len2 = len(nums1), len(nums2)
        if (len1 + len2) % 2 == 1:
            return Solution.findKth(self, nums1, len1, nums2, len2, (len1 + len2) / 2 + 1)
        else:
            return (Solution.findKth(self, nums1, len1, nums2, len2, (len1 + len2) / 2) + \
                    Solution.findKth(self, nums1, len1, nums2, len2, (len1 + len2) / 2 + 1)) / 2.0

#solution = Solution()
#print solution.findMedianSortedArrays([1, 2], [3])
