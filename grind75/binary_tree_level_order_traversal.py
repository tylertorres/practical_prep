# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque([root])
        levels = []
        
        while queue and root:
            sz = len(queue)
            current_level = []
            
            for _ in range(sz):
                node = queue.popleft()
                current_level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            levels.append(current_level)
        
        return levels


"""


steps
1. Form queue
2. get length q at current time
3. pop from queue sz times 
4. maintain a level 
"""
