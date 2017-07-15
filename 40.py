class Solution(object):
    def combinationSum2(self, candidates, target):
        res = []
        if not candidates:
            return res
        candidates.sort()
        Solution.foo(self, candidates, 0, target, [], res)
        return res

    def foo(self, candidates, index, target, cur, res):
        if target < 0:
            return
        if target == 0:
            res.append(cur[:])
        for i in xrange(index, len(candidates)):
            if i > index and candidates[i] == candidates[i - 1]:
                continue
            cur.append(candidates[i])
            Solution.foo(self, candidates, i + 1, target - candidates[i], cur, res)
            del cur[-1]

print Solution().combinationSum([10, 1, 2, 7, 6, 1, 5], 8)
