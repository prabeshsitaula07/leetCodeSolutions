class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        def dfs(node, is_root):
            if not node:
                return None
            
            delete_current = node.val in to_delete
            
            node.left = dfs(node.left, is_root=delete_current)
            node.right = dfs(node.right, is_root=delete_current)
            
            if delete_current:
                if node.left:
                    forest.append(node.left)
                if node.right:
                    forest.append(node.right)
                return None
            else:
                return node
        
        forest = []
        root = dfs(root, is_root=True)
        
        if root:
            forest.append(root)
            
        return forest