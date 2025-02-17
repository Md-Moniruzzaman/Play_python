
import graphviz

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left =  self.right = None
    def __str__(self):
        return str(self.key)
    def __repr__(self):
        return 'Node: ' + str(self.key)
       

def insert(root, key):

    if root is None:
        return TreeNode(key)
    else:
        if key < root.key:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)

    return root

def visialize_binary_tree(root):
    dot = graphviz.Digraph(comment='Binary tree')
    dot.node(str(root.key))

    def add_nodes_edges(node):
        if node.left:
            dot.node(str(node.left.key))
            dot.edge(str(node.key),str(node.left.key),)
            add_nodes_edges(node.left)
        if node.right:
            dot.node(str(node.right))
            dot.edge(str(node.key), str(node.right.key))
            add_nodes_edges(node.right)

    add_nodes_edges(root)
    dot.render('binary_tree', view=True, format='png')
    

root = None
keys = [5, 3, 7, 2, 4, 6, 8]
for key in keys:
    root = insert(root, key)

visialize_binary_tree(root)

