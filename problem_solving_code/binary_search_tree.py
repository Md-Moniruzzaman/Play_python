class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = self.right =None

class Solution:
    def insert(self, root, data):
        if root is None:
            return TreeNode(data)
        else:
            if data < root.data:
                curr = self.insert(root.left, data)
                root.left = curr
            else:
                curr = self.insert(root.right, data)
                root.rihgt = curr

        return root
    def getHeight(self, root):
        if root is None:
            return -1

        hl = self.getHeight(root.left)
        hr = self.getHeight(root.right)

        if hl>hr:
            return 1 + hl
        else:
            return 1 + hr
        
T = int(input())
myTree = Solution()
root = None
for i in range(T):
    data = int(input())
    root = myTree.insert(root, data)

height = myTree.getHeight(root)
print(f'Height of binary search: {height}')

