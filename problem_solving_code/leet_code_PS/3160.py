"""
    Find the number of distict colors among the balls 
"""

from collections import defaultdict

def queryResults( limit: int, queries: list[list[int]]) -> list[int]:

    ball_colors = {}  
    color_count = defaultdict(int)  
    current_distinct = 0  
    result = []
    
    for a, b in queries:
        prev_color = ball_colors.get(a)
        
        if prev_color is not None:
            color_count[prev_color] -= 1
            if color_count[prev_color] == 0:
                current_distinct -= 1
                
        if color_count[b] == 0:
            current_distinct += 1
        color_count[b] += 1
        ball_colors[a] = b
        
        result.append(current_distinct)
    
    return result
            
print(queryResults(4, [[1,4],[2,5],[1,3],[3,4]]))