from collections import defaultdict

class Solution:
    def mostProfitablePath(self, edges: list[list[int]], bob: int, amount: list[int]) -> int:
        # Step 1: Build the tree as an adjacency list
        tree = defaultdict(list)
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)

        # Step 2: Find Bob's path to root (0) using DFS
        time_bob = {i: float('inf') for i in range(len(amount))}
        
        def find_bob_path(node, parent, time):
            """ Computes how long Bob takes to reach each node. """
            if node == bob:
                time_bob[node] = 0  # Bob starts here
            
            for neighbor in tree[node]:
                if neighbor == parent:
                    continue
                find_bob_path(neighbor, node, time + 1)
                time_bob[node] = min(time_bob[node], time_bob[neighbor] + 1)

        find_bob_path(0, -1, 0)  # Start DFS from root (node 0)

        # Step 3: DFS to find max profit path for Alice
        max_profit = float('-inf')
        
        def dfs_alice(node, parent, time, current_profit):
            """ DFS to find the max profit path for Alice. """
            nonlocal max_profit

            # Handle Alice’s earnings based on Bob’s time
            if time < time_bob[node]:  # Alice arrives first
                current_profit += amount[node]
            elif time == time_bob[node]:  # Alice and Bob arrive together
                current_profit += amount[node] // 2  # Half amount
            # If Bob reached first, Alice gets 0, so no change in profit
            
            # If leaf node, update max profit
            if len(tree[node]) == 1 and node != 0:  # Ignore root
                max_profit = max(max_profit, current_profit)

            # Explore further paths
            for neighbor in tree[node]:
                if neighbor == parent:
                    continue
                dfs_alice(neighbor, node, time + 1, current_profit)

        dfs_alice(0, -1, 0, 0)  # Start DFS for Alice from node 0

        return max_profit


edges = [[0,1], [1,2], [1,3], [3,4], [3,5]]
bob = 3
amount = [-2, 4, 2, -4, 6, 8]
obj = Solution()
print(obj.mostProfitablePath(edges, bob, amount))  # Output: Maximum profit
     
     
'''      0
        |
        1
       / \
      2   3 (Bob starts here)
         / \
        4   5
'''