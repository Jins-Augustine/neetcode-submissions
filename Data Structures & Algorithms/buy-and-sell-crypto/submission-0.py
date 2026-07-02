class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        res = float("-inf")
        for i in range(len(prices)):
            j=len(prices)-1
            while i<j:
                profit = prices[j] - prices[i]
                res = max(res,profit)
                j -= 1
        if res<0:
            return 0
        else:
            return res