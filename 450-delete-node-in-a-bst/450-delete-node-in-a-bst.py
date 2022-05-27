# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        if root is None:
            return None
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
            
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
            
        else:
            if root.left is None and root.right is None:
                root = None
                return None
            
            elif root.left != None and root.right == None:
                root = root.left
                return root
            
            if root.left == None and root.right != None:
                root = root.right
                return root
            
            else:
                
                #subsNode = TreeNode()
                subsNode = self.findMinNode(root.right)

                root.val = subsNode.val

                root.right = self.deleteNode(root.right, subsNode.val)
            
        return root
    
    def findMinNode(self, root):
        current = root
        
        while current.left != None:
            current = current.left
            
        return current
            
        