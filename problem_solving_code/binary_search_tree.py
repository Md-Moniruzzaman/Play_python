import graphviz

class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = self.right =None

    def __str__(self) -> str:
        return str(self.data)

class Solution:
   
    def insert(self,root,data):
        if root is None:
            return TreeNode(data)
        else:
            if data <= root.data:
                cur = self.insert(root.left, data)
                root.left = cur
            else:
                cur = self.insert(root.right, data)
                root.right = cur
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
        

def visialize_binary_tree(root):
    dot = graphviz.Digraph()
    dot.node(str(root.data))

    def add_nodes_edges(node):
        if node.left:
            dot.node(str(node.left.data))
            dot.edge(str(node.data),str(node.left.data),)
            add_nodes_edges(node.left)
        if node.right:
            dot.node(str(node.right))
            dot.edge(str(node.data), str(node.right.data))
            add_nodes_edges(node.right)

    add_nodes_edges(root)
    dot.render('binary_tree', view=True, format='png')
    
        
T = int(input())
myTree = Solution()
root = None
for i in range(T):
    data = int(input())
    root = myTree.insert(root, data)

height = myTree.getHeight(root)
# visialize_binary_tree(root)
print(f'Height of binary search: {height}')




# class Node:
#     def __init__(self,data):
#         self.right=self.left=None
#         self.data = data
# class Solution:
#     def insert(self,root,data):
#         if root==None:
#             return Node(data)
#         else:
#             if data<=root.data:
#                 cur=self.insert(root.left,data)
#                 root.left=cur
#             else:
#                 cur=self.insert(root.right,data)
#                 root.right=cur
#         return root

#     def getHeight(self,root):
#         if root is None:
#             return -1

#         hl = self.getHeight(root.left)
#         hr = self.getHeight(root.right)

#         if hl>hr:
#             return 1 + hl
#         else:
#             return 1 + hr

# T=int(input())
# myTree=Solution()
# root=None
# for i in range(T):
#     data=int(input())
#     root=myTree.insert(root,data)
# height=myTree.getHeight(root)
# print(height)       