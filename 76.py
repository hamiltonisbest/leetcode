from collections import defaultdict

class Solution(object):
    def minWindow(self, s, t):
        needed = defaultdict(int)
        for c in t:
            needed[c] += 1
        missing = len(t)
        i, left, right = 0, 0, 0
        for j, c in enumerate(s, 1):
            if needed[c] > 0:
                missing -= 1
            needed[c] -= 1
            if missing == 0:
                while i < j and needed[s[i]] < 0:
                    needed[s[i]] += 1
                    i += 1
                if right == 0 or j - i < right - left:
                    left, right = i, j
        return s[left:right]

print Solution().minWindow("ADBCAD", "ABC")
