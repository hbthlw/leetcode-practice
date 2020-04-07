# coding=utf-8
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        result = []

        def search(node, path):
            if not node:
                return
            path += str(node.val)
            # 如果左右子树都没有，退出递归
            if not node.left and not node.right:
                result.append(path)
                return
            path += '->'
            if node.left:
                search(node.left, path)
            if node.right:
                search(node.right, path)

        search(root, '')

        return result


if __name__ == '__main__':
    root = TreeNode('1')
    leaf_2 = TreeNode('2')
    leaf_3 = TreeNode('3')
    leaf_5 = TreeNode('5')
    root.left = leaf_2
    root.right = leaf_3
    leaf_2.right = leaf_5
    print Solution().binaryTreePaths(root)
