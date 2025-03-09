'''Find How many alternatives are there for a group of circle of colors'''

def numberOfAlternatingGroups(colors: list[int], k:int) -> int:
    # Initialize variables
    n = len(colors)
    count = 0
    left = 0
    
    # Count the number of alternating groups
    for right in range(1, n+k-1):
        if colors[right%n] == colors[(right - 1)%n]:
            left = right
        if right - left + 1 > k:
            left += 1
        if right - left + 1 == k:
            count += 1
    
    return count

# Test Cases
print(numberOfAlternatingGroups([0,1,0,1,0], 3)) # 3
print(numberOfAlternatingGroups([0,1,0,0,1,0,1], 6)) # 2
print(numberOfAlternatingGroups([1,1,1,1,1,1,1,1], 2)) # 0