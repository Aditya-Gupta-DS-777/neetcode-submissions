class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n={}
        for c in nums:
            if c not in n:
                n[c] = 1
            n[c] += 1
        arr = []
        for num, cnt in n.items():
            arr.append([cnt, num])
        arr.sort()
        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res
        