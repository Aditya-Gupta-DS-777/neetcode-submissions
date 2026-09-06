class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        r=0
        for i  in range(len(prices)-1):
            b=prices[i]
            for j in range(i+1,len(prices)):
                s=prices[j]
                r=max(r,s-b)
        return r


       