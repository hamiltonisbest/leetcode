class Solution(object):
    def longestValidParentheses(self, s):
        if not s:
            return 0
        st = [-1]
        max_len = 0
        for i, c in enumerate(s):
            if c == '(':
                st.append(i)
            else:
                if len(st) > 1:
                    del st[-1]
                    max_len = max(max_len, i - st[-1])
                else:
                    st[-1] = i
        return max_len

print Solution().longestValidParentheses("())()")
