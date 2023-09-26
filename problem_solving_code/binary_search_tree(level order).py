class TreeNode:
    def __init__(self,data) -> None:
        self.data = data
        self.left = self.right = None
class Solution:
    def insert(self, root, data):
        if root is None:
            return TreeNode(data)
        else:
            if data<=root.data:
                cur = self.insert(root.left, data)
                root.left = cur
            else:
                cur = self.insert(root.right, data)
                root.right = cur
        return root
    
    def levelOrder(self, root):
        q = []
        q.append(root)
        while len(q) != 0:
            root = q.pop(0)
            print(root.data, end=' ')
            if root.left  is not None:
                q.append(root.left)
            if root.right is not None:
                q.append(root.right)

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)