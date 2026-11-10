# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def __init__(self):
        self.max_sum = float("-inf")

    def find_max_sum(self, root):
        if not root:
            return 0
        if not root.left and not root.right:
            self.max_sum = max(self.max_sum, root.val)
            return root.val
        
        left = max(0, self.find_max_sum(root.left))
        right = max(0, self.find_max_sum(root.right))

        self.max_sum = max(self.max_sum, left + right + root.val)

        return root.val + max(left, right)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        self.find_max_sum(root)

        return self.max_sum