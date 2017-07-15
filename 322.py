class Solution(object):
    def coinChange(self, coins, amount):
        if amount < 0 or not coins:
            return -1
        dp = [amount + 1 for i in xrange(amount + 1)]
        dp[0] = 0
        for x in coins:
            for i in xrange(x, amount + 1):
                dp[i] = min(dp[i], dp[i - x] + 1)
        return -1 if dp[amount] == amount + 1 else dp[amount]

print Solution().coinChange([2], 3)
