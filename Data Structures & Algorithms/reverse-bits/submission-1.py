
class Solution:
    def reverseBits(self, n: int) -> int:
        res = ""

        for i in range(32):
            bit = n & 1
            res += str(bit)
            n >>= 1

        decimal = 0
        for bit in res:
            decimal = decimal * 2 + int(bit)

        return decimal
