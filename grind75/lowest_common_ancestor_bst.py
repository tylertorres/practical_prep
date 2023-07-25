# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        evaluation, ancestor = dfs(root, p, q)
        return ancestor


def dfs(root: "TreeNode", p: "TreeNode", q: "TreeNode"):
    if root is None:
        return False, None

    left, left_ancestor = dfs(root.left, p, q)
    right, right_ancestor = dfs(root.right, p, q)

    if left_ancestor is not None or right_ancestor is not None:
        return True, left_ancestor if left_ancestor else right_ancestor

    child = False
    isAncestorChild = root.val == p.val or root.val == q.val

    if left or right:
        child = True

    if (child and isAncestorChild) or (left and right):
        return True, root

    return child or isAncestorChild, None


def lowestCommonAncestorV2(
    self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
) -> "TreeNode":
    while True:
        if root.val > p.val and root.val > q.val:
            root = root.left
        elif root.val < p.val and root.val < q.val:
            root = root.right
        else:
            return root
