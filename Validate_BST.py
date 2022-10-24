# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        self.result = []  #to append the node value in the list
        self.inorder(root)  #calling and passing the root in the recursion
        
        for i in range(1,len(self.result)):  #checking whether the numbers are in ascending order, if the numbers are not in ascending order return false else returning true
            
            if self.result[i-1]<self.result[i]:
                pass
            
            else:
                return False
            
        return True
        
        
    def inorder(self,root):  #recursion function
        if root == None:  #if the root is null the recurrsion starts to unfold
            return
        
        
        self.inorder(root.left)  #recurrsion for the left side of the root
        
        self.result.append(root.val)  #appending the root value
        
        self.inorder(root.right)  #recurrsion for the left side of the root
        