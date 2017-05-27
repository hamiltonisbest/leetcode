class Solution(object):
    def threeSum(self, nums):
        if not nums:
            return []
        positives, negatives = [], []
        zero_cnt = 0
        pos_set, neg_set = set(), set()
        for x in nums:
            if x > 0:
                pos_set.add(x)
                positives.append(x)
            elif x == 0:
                zero_cnt += 1
            else:
                neg_set.add(x)
                negatives.append(x)
        triplet_set = set()
        if zero_cnt >= 3:
            triplet_set.add((0, 0, 0))
        if zero_cnt > 0:
            for x in positives:
                if -x in neg_set and (-x, 0, x) not in triplet_set:
                    triplet_set.add((-x, 0, x))
        for i in xrange(len(positives)):
            for j in xrange(i + 1, len(positives)):
                x, y = min(positives[i], positives[j]), max(positives[i], positives[j])
                if -x - y in neg_set and (-x - y, x, y) not in triplet_set:
                    triplet_set.add((-x - y, x, y))
        for i in xrange(len(negatives)):
            for j in xrange(i + 1, len(negatives)):
                x, y = min(negatives[i], negatives[j]), max(negatives[i], negatives[j])
                if -x - y in pos_set and (x, y, -x - y) not in triplet_set:
                    triplet_set.add((x, y, -x -y))
        ans = []
        for t in triplet_set:
            ans.append(list(t))
        return ans

solution = Solution()
print solution.threeSum([-1, 0, 0, 0, 1])
