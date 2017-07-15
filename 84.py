class Solution(object):
    def largestRectangleArea(self, heights):
        if not heights:
            return 0
        heights.append(0)
        max_area = 0
        st = [-1]
        for i, x in enumerate(heights):
            while heights[st[-1]] > x:
                height, width = heights[st.pop()], i - st[-1] - 1
                max_area = max(max_area, height * width)
            st.append(i)
        return max_area

print Solution().largestRectangleArea([2,1,5,6,2,3])
