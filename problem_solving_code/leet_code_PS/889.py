'''Constrack Binary Tree form Preorder and Postorder Traversal'''

from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def constructFromPrePost(self, preorder: list[int], postorder: list[int]) -> TreeNode:
        stack = []
        i = 1
        stack.append(TreeNode(preorder[0]))
        while i< len(preorder):
            node = TreeNode(preorder[i])
            if preorder[i] > preorder[i-1]:
                if stack and not stack[-1].left:
                    stack[-1].left = node
                elif stack:
                    stack[-1].right = node
            else:
                while len(stack)>1:
                    stack.pop()
                if stack and not stack[-1].left:
                    stack[-1].left = node
                elif stack:
                    stack[-1].right = node
                
            stack.append(node)
            i+=1
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
root = obj.constructFromPrePost([1,2,4,5,3,6,7], [4,5,2,6,7,3,1])
print(obj.treeToList(root))  # Output: [1, 2, 3, 4, 5, 6, 7]
# root = obj.constructFromPrePost("1-2--3---4-5--6---7")
# print(obj.treeToList(root))  # Output: [1, 2, 5, 3, 4, 6, 7]
