# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root)[1]
    
    def dfs(self, root: Optional[TreeNode]):
        if root is None:
            return 0, 0
        
        left, left_max = self.dfs(root.left)
        right, right_max = self.dfs(root.right)

        max_including_root = left + right
        max_excluding_root = max(left, right) + 1

        return max_excluding_root, max(left_max, right_max, max_including_root)
