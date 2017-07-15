class Solution(object):
    def maximalRectangle(self, matrix):
        if not matrix:
            return 0
        height, width = len(matrix), len(matrix[0])
        dp = [0] * (width + 1)
        ans = 0
        for i in xrange(height):
            for j in xrange(width):
                if matrix[i][j] == 1:
                    dp[j] += 1
                else:
                    dp[j] = 0
            ans = max(ans, Solution.getMaxHistogram(self, dp))
        return ans

    def getMaxHistogram(self, height):
        st = [-1]
        ans = 0
        for i, x in enumerate(height):
            while height[st[-1]] > x:
                h = height[st[-1]]
                del st[-1]
                ans = max(ans, h * (i - st[-1] - 1))
            st.append(i)
        return ans

matrix = [[1, 0, 1, 0, 0], [1, 0, 1, 1, 1], [1, 1, 1, 1, 1], [1, 0, 0, 1, 0]]
print Solution().maximalRectangle(matrix)
