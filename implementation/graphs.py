# DFS - depth first search

# inorder traversal
from warnings import warn


def inorderTraversal(root: Optional[TreeNode]) -> List[int]:
    res = []
    def dfs(node):
        if node == None:
            return
        

        dfs(node.left)
        res.append(node.val)
        dfs(node.right)

    dfs(root)
    return res

# max depth of a binary tree
def maxDepth(root: Optional[TreeNode]) -> int:
    def calculateMaxDepth(node):
        if node == None:
            return 0
        return 1 + max(calculateMaxDepth(node.left), calculateMaxDepth(node.right))
    return calculateMaxDepth(root)


