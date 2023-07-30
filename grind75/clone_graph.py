"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return node

        cloned_root_node = Node(node.val)
        queue = deque([(node, cloned_root_node)])
        cloned_nodes = {cloned_root_node.val: cloned_root_node}

        while queue:
            node, cloned_node = queue.popleft()

            for neighbor in node.neighbors:
                if neighbor.val not in cloned_nodes:
                    cloned_nodes[neighbor.val] = Node(neighbor.val)
                    queue.append((neighbor, cloned_nodes[neighbor.val]))
                
                cloned_node.neighbors.append(cloned_nodes[neighbor.val])
                
        return cloned_root_node






        



"""
- from the starting node, look at neighbors
    - if neighbors are not visited : add them to Q and add them to visited
    - else : just add them to the neighbors of the current node and continue

"""
