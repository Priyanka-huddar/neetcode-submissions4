# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def postOrder(root):
            if root is None:
                return []
            postorder=[]
            st1=[]
            st2=[]
            st1.append(root)
            while st1:
                root=st1.pop()
                st2.append(root)

                if root.left:
                    st1.append(root.left)
                if root.right:
                    st1.append(root.right)
            while st2:
                postorder.append(st2.pop().val)
            return postorder
        return postOrder(root)