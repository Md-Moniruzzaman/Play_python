def maxArea(height: list[int])->int:
    # LINEAR TIME SOLUTION: O(n)
    left = 0
    right = len(height) - 1
    maxarea = 0
    
    while left<right:
        current_area = min(height[left], height[right]) * (right-left)
        maxarea = max(maxarea, current_area)
        
        if height[left] < height[right]:
            left+=1
        else:
            right-=1
            
    return maxarea

print(maxArea([8,7,2,1]))
        