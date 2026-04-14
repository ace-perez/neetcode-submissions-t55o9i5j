# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, node: Optional[TreeNode], low: int, high: int) -> int:
        if not node:
            return 0
        
        if node.val > high:
            return self.rangeSumBST(node.left, low, high)
        
        if node.val < low:
            return self.rangeSumBST(node.right, low, high)
        
        return node.val + self.rangeSumBST(node.left, low, high) + self.rangeSumBST(node.right, low, high)