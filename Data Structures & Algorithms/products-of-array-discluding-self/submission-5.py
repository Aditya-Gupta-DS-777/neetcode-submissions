class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = []
        suf = []
        res = [1] * n

        ps = 1
        for i in nums:
            ps *= i
            pre.append(ps)

        ss = 1
        for i in range(n - 1, -1, -1):
            ss *= nums[i]
            suf.append(ss)

        suf.reverse()

        for k in range(n):
            left = pre[k - 1] if k > 0 else 1
            right = suf[k + 1] if k < n - 1 else 1
            res[k] = left * right

        return res