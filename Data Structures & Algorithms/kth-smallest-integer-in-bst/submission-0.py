# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        inorder_array = []

        self.dfs(inorder_array, root)

        return inorder_array[k-1]
    
    def dfs(self, inorder_array, node):
        if not node:
            return
        
        self.dfs(inorder_array, node.left)
        inorder_array.append(node.val)
        self.dfs(inorder_array, node.right)
