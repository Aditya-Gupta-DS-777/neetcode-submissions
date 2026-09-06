class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hash={}
        for i,j in enumerate(nums):
            remain=target-j
            if remain in hash:
                return [hash[remain],i]
            hash[j]=i