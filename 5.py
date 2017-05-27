class Solution(object):
    def longestPalindrome(self, s):
        if s == "":
            return s
        n = len(s)
        dp = [False] * n
        start, end, max_len = 0, 0, 1
        for i in xrange(n):
            dp[i] = True
            for j in xrange(i):
                if s[i] == s[j] and (i - j == 1 or dp[j + 1]):
                    dp[j] = True
                    if i - j + 1 > max_len:
                        max_len = i - j + 1
                        start, end = j, i
                else:
                    dp[j] = False
        return s[start : end + 1]

solution = Solution()
print solution.longestPalindrome("cbbd")
