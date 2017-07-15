class Solution(object):
    def minDistance(self, word1, word2):
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)
        n1, n2 = len(word1), len(word2)
        dp = [[0] * (n2 + 1) for i in xrange(n1 + 1)]
        for i in xrange(n1 + 1):
            dp[i][0] = i
        for i in xrange(n2 + 1):
            dp[0][i] = i
        for i in xrange(1, n1 + 1):
            for j in xrange(1, n2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
        return dp[n1][n2]

print Solution().minDistance("ACB", "BB")
