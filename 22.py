class Solution(object):
    def generateParenthesis(self, n):
        if n <= 0:
            return []
        res = []
        Solution.do_generate(self, n, n, '', res)
        return res

    def do_generate(self, left, right, s, res):
        if left == 0 and right == 0:
            res.append(s)
        if left > 0:
            Solution.do_generate(self, left - 1, right, s + '(', res)
        if right > 0 and right > left:
            Solution.do_generate(self, left, right - 1, s + ')', res)

print Solution().generateParenthesis(1)
