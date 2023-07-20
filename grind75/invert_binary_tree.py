# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = deque([root])

        while queue:
            queue_size = len(queue)
            for _ in range(queue_size):
                node = queue.popleft()
                if node:
                    node.left, node.right = node.right, node.left
                    add_children_to_queue(queue, node)
                
        return root

def add_children_to_queue(queue, node):
    if node.left:
        queue.append(node.left)
    if node.right:
        queue.append(node.right)


