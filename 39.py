class Solution(object):
    def combinationSum(self, candidates, target):
        res = []
        if not candidates:
            return res
        Solution.foo(self, candidates, 0, target, [], res)
        return res

    def foo(self, candidates, index, target, cur, res):
        if target < 0:
            return
        if target == 0:
            res.append(cur[:])
        for i in xrange(index, len(candidates)):
            cur.append(candidates[i])
            Solution.foo(self, candidates, i, target - candidates[i], cur, res)
            del cur[-1]

print Solution().combinationSum([2, 3, 6], 7)
