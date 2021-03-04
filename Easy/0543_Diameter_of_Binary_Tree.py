# Given a binary tree, you need to compute the length of the diameter of the tree.
# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
#
# Example:
# Given a binary tree
#           1
#          / \
#         2   3
#        / \
#       4   5
# Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].
#
# Note: The length of path between two nodes is represented by the number of edges between them.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0

        leftdis, rightdis, selfdis = 0, 0, 0

        if root.left:
            leftdis = self.diameterOfBinaryTree(root.left)

        if root.right:
            rightdis = self.diameterOfBinaryTree(root.right)

        selfdis = self.depth(root.left) + self.depth(root.right)

        print(selfdis, leftdis, rightdis)

        return max(selfdis, leftdis, rightdis)

    def depth(self, root: TreeNode) -> int:
        if not root:
            return 0
        elif root.left and root.right:
            return 1 + max(self.depth(root.left), self.depth(root.right))
        elif root.left:
            return 1 + self.depth(root.left)
        elif root.right:
            return 1 + self.depth(root.right)
        else:
            return 1