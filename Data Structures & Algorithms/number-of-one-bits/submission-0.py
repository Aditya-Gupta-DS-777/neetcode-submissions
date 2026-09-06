class Solution:
    def hammingWeight(self, n: int) -> int:
        binary = bin(n)[2:]
        binary=list(binary)
        count=0
        for i in binary:
            if i=='1':
                count+=1
        return count
            
        