# ''' Recover the Tree from Preorder Traversal'''

# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def recoverFromPreorder(self, traversal: str) -> TreeNode:
#         dash = 0
#         stack = []
#         i = 0
#         while i < len(traversal):
#             if traversal[i] == "-":
#                 i+=1
#                 dash+=1
#             else:
#                 k = i
#                 while k < len(traversal) and traversal[k] != "-":
#                     k+=1
#                 val = int(traversal[i:k])
#                 node = TreeNode(val= val)
                
#                 while len(stack) > dash:
#                     stack.pop()
                
#                 if stack and not stack[-1].left:
#                     stack[-1].left = node
#                 elif stack:
#                     stack[-1].right = node
#                 stack.append(node)
#                 dash = 0
#                 i = k
#         return stack[0]
    
# # Example usage:
# obj = Solution()
# root = obj.recoverFromPreorder("1-2--3--4-5--6--7")

# print(root.val)           # 1
# print(root.left.val)      # 2
# print(root.left.left.val) # 3
# print(root.left.right.val)# 4
# print(root.right.val)     # 5
# print(root.right.left.val)# 6
# print(root.right.right.val)# 7
                
                
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverFromPreorder(self, traversal: str) -> TreeNode:
        dash = 0
        stack = []
        i = 0
        while i < len(traversal):
            if traversal[i] == "-":
                i += 1
                dash += 1
            else:
                k = i
                while k < len(traversal) and traversal[k] != "-":
                    k += 1
                val = int(traversal[i:k])  # ✅ Convert to integer
                node = TreeNode(val=val)
                
                while len(stack) > dash:
                    stack.pop()
                
                if stack and not stack[-1].left:
                    stack[-1].left = node
                elif stack:
                    stack[-1].right = node
                stack.append(node)
                dash = 0
                i = k
        return stack[0]

    def treeToList(self, root: TreeNode):
        """ Convert the tree to a list using level-order traversal (BFS). """
        if not root:
            return []
        
        result = []
        queue = deque([root])

        while queue:
            node = queue.popleft()
            if node:
                result.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append(None)  # Use `None` to indicate missing children
        
        # Remove trailing `None` values for cleaner output
        while result and result[-1] is None:
            result.pop()
        
        return result

# Example usage:
obj = Solution()
root = obj.recoverFromPreorder("1-2--3--4-5--6--7")
print(obj.treeToList(root))  # Output: [1, 2, 5, 3, 4, 6, 7]
root = obj.recoverFromPreorder("1-2--3---4-5--6---7")
print(obj.treeToList(root))  # Output: [1, 2, 5, 3, 4, 6, 7]
