class Solution(object):
    def longestPalindrome(self, s):
        t = ['$', '#']
        for c in s:
            t.append(c)
            t.append('#')
        t.append('?')
        farest, idx, max_len, center = 0, 0, 0, 0
        p = [0] * len(t)
        for i in xrange(1, len(t) - 1):
            p[i] = min(p[2 * idx - i], farest - i) if farest > i else 1
            while t[i + p[i]] == t[i - p[i]]:
                p[i] += 1
            if farest < i + p[i]:
                farest = i + p[i]
                idx = i
            if max_len < p[i]:
                max_len = p[i]
                center = i
        return s[(center - max_len) / 2 : (center - max_len) / 2 + max_len - 1]

solution = Solution()
print solution.longestPalindrome("babbb")
