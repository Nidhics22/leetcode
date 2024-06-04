# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Method 1: Iterative Solution
        res = []  # Global variable for both methods
        stack = []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
        return res

        # Method 2: Recursive Solution
        def inorder(root):
            while not root:
                return

            inorder(root.left)
            res.append(root.val)
            inorder(root.right)

        inorder(root)
        return res
