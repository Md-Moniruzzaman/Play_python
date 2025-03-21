from collections import deque
from typing import List

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = {}  # Ingredient → Recipes that depend on it
        in_degree = {}  # Recipe → Number of missing ingredients
        
        # Initialize in-degree and graph
        for recipe, ing_list in zip(recipes, ingredients):
            in_degree[recipe] = len(ing_list)  # Each recipe initially needs all its ingredients
            for ing in ing_list:
                if ing not in graph:
                    graph[ing] = []
                graph[ing].append(recipe)  # Dependency: ing → recipe
        
        # Queue with initial supplies
        queue = deque(supplies)
        result = set(supplies)  # Already available items
        print(queue, result)
        
        # Process the queue (Topological Sort)
        while queue:
            item = queue.popleft()
            
            # If item is an ingredient in recipes, update dependencies
            if item in graph:
                for recipe in graph[item]:
                    in_degree[recipe] -= 1  # Reduce missing ingredients count
                    
                    # If all ingredients are available, we can make the recipe
                    if in_degree[recipe] == 0:
                        queue.append(recipe)
                        result.add(recipe)  # Mark it as craftable
        
        # Return only the recipes that can be made
        return [r for r in recipes if r in result]
# Example
s = Solution()
print(s.findAllRecipes(recipes = ["bread"], ingredients = [["yeast","flour"]], supplies = ["yeast","flour","corn"]))