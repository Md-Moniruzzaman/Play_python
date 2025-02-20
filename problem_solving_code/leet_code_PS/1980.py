

def findDifferentBinaryString(nums: list[str]) -> str:
    val = len(nums[0])  
    total_occurrence = 2 ** val  # Calcualte total occurence binary number

    for i in range(total_occurrence):
        ans = '{:0{}b}'.format(i, val)  # Convert integer to binary
        print(ans)
        if ans not in nums: # Check and if not exist return value
            return ans

            
print(findDifferentBinaryString(["01","10"]))