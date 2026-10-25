class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_a = 0

        i = 0
        j = len(heights) - 1

        while i != j:
            if heights[i] > heights[j]:
                if (heights[j] * (j - i) > max_a):
                    max_a = heights[j] * (j - i)
                j -= 1
            else:
                if (heights[i] * (j - i) > max_a):
                    max_a = heights[i] * (j - i)
                i += 1
        return max_a

