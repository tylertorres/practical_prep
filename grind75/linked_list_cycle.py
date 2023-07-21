# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        new_head = ListNode(float('inf'))
        new_head.next = head

        left = right = new_head

        while right and right.next:
            left = left.next
            right = right.next.next

            if left == right:
                return True

        return False

"""
3 => 2 => 0 => -4
     ^
     -4
          l
    r

Steps
1. Move left pointer 1
2. move right pointer 2
3. check if node at p1 and p2 are the same
    1 yes : return True
    2 no : continue iteration
4. 
"""

