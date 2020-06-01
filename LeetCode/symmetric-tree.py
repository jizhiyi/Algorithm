# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 递归
# class Solution:
#     def issame(self, l, r):
#         # 两个都不为None
#         if not l and not r:
#             return True
#         # 有一个为None
#         if not l or not r:
#             return False
#         return l.val == r.val and self.issame(l.left, r.right) and self.issame(l.right, r.left)

#     def isSymmetric(self, root: TreeNode) -> bool:
#         return self.issame(root, root)

# 迭代
import queue
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        q = queue.Queue()
        q.put((root.left, root.right))
        while not q.empty():
            l, r = q.get()
            # print('pre', None if l is None else l.val, None if r is None else r.val)
            if not l and not r:
                continue
            if not l or not r or l.val != r.val:
                return False
            # print(None if l.left is None else l.left.val, None if r.right is None else r.right.val)
            # print(None if l.right is None else l.right.val, None if r.left is None else r.left.val)
            q.put((l.left, r.right))
            q.put((l.right, r.left))
        return True


# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(2)
# root.left.left = TreeNode(3)
# root.left.right = TreeNode(4)
# root.right.left = TreeNode(4)
# root.right.right = TreeNode(3)
# print(Solution().isSymmetric(root))

root = TreeNode(2)
root.left = TreeNode(3)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(4)
print(Solution().isSymmetric(root))