class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if s == "":
            return 0
        n = len(s)
        dp = [0] * n
        nearest = [-1] * 256
        ans = 1
        dp[0] = 1
        nearest[ord(s[0])] = 0
        for i in xrange(1, n):
            if nearest[ord(s[i])] < i - dp[i - 1]:
                dp[i] = dp[i - 1] + 1
            else:
                dp[i] = i - nearest[ord(s[i])]
            nearest[ord(s[i])] = i
            ans = max(ans, dp[i])
        return ans

#solution = Solution()
#print solution.lengthOfLongestSubstring('aaabbaa')
