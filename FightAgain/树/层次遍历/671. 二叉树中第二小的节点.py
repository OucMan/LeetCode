# 题目

给定一个非空特殊的二叉树，每个节点都是正数，并且每个节点的子节点数量只能为 2 或 0。如果一个节点有两个子节点的话，那么该节点的值等于两个子节点中较小的一个。

更正式地说，root.val = min(root.left.val, root.right.val) 总成立。

给出这样的一个二叉树，你需要输出所有节点中的第二小的值。如果第二小的值不存在的话，输出 -1 。

# 思路

假如根节点为空，直接返回-1，假如根节点没有子节点，直接返回-1，然后保存左右两个子节点的值L,R，假如L和根节点的值一样大，那么对于对于整棵树来说，第二小节点可能也是左子树的第二小节点，同理，对于右子树也是这样，使用递归得到两个子树的第二小节点，然后再进一步比较得到最终的答案


# 代码

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return -1
        if not root.left and not root.right:
            return -1
        l, r = root.left.val, root.right.val
        if l == root.val:
            l = self.findSecondMinimumValue(root.left)
        if r == root.val:
            r = self.findSecondMinimumValue(root.right)
        if l != -1 and r != -1:
            return min(l, r)
        if l != -1:
            return l
        return r
        
        
