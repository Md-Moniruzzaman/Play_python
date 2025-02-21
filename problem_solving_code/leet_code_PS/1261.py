''' Find Eelement in a contaminated Binary Tree'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class FindElements:

    def __init__(self, root: TreeNode):
        self.values = set()
        self.recovered_tree(root, 0)
        
    def recovered_tree(self, node: TreeNode,  x: int)->None:
        if not node:
            return
        
        print(node)
        self.val = x
        self.values.add(x)
        self.recovered_tree(node.left , 2*x+1)
        self.recovered_tree(node.right , 2*x+2)
        

    def find(self, target: int) -> bool:
        return target in self.values


# Your FindElements object will be instantiated and called as such:
# Creating a contaminated tree (-1 values everywhere)
# root = TreeNode(-1, TreeNode(-1, TreeNode(-1), TreeNode(-1)), TreeNode(-1))
root = TreeNode(-1, None, TreeNode(-1))

# Initialize the FindElements class (recovers the tree)
finder = FindElements(root)

# Check if values exist
print(finder.find(1))  # True
print(finder.find(2))  # True
print(finder.find(5))  # False
