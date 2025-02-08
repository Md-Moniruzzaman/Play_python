
"""
    - Changing the same index to the same number multiple times → no change.

    - Changing an index multiple times to different numbers, then back.

    - find for numbers that have had their indexes changed.
    
    Approach
    The approach involves using two primary data structures:

    Index Mapping: A dictionary to keep track of the current number at each index.

    Number Heaps: A dictionary where each key is a number and the value is a min-heap of indices. This allows efficient retrieval of the smallest index for any given number.

    Operations:

    Change Operation: When inserting or replacing a number at an index, update the index mapping and push the index into the corresponding number's heap. If the index was previously associated with another number, the old number's heap is not modified directly but will be cleaned up lazily during subsequent find operations.

    Find Operation: For a given number, check the corresponding heap. Remove invalid indices (those that no longer hold the number) from the heap until a valid index is found or the heap is empty.
"""

import heapq
from collections import defaultdict

class NumberContainers:

    def __init__(self):
        self.index_map = {} # Maps each indices to its courrent number
        self.number_heaps = defaultdict(list) # Maps each number to its min-heap indices
        

    def change(self, index: int, number: int) -> None:
        # if the index has the same number, no change needed
        if self.index_map.get(index, None) == number:
            return
        
        # Update index with new number
        self.index_map[index] = number
        
        # Push the current index into the new number's heap
        heapq.heappush(self.number_heaps[number], index)
        

    def find(self, number: int) -> int:
        # If the number has no entries in the heap, return -1
        if number not in self.number_heaps:
            return -1
        
        heap = self.number_heaps[number]
        
        # Process the heap to find the smallest valid index
        while heap:
            cur_index = heap[0]
            # Check if cur_index is still maped to the target number
            if self.index_map.get(cur_index, None) == number:
                return cur_index
            else:
                # Remove the invalid index from the heap
                heapq.heappop(heap)
                
        return -1
        


# Your NumberContainers object will be instantiated and called as such:
if __name__ == "__main__":
    obj = NumberContainers()
    
    method_call = ["NumberContainers","find","change","change","change","change","find","change","find"]
    number_container = [[],[10],[2,10],[1,10],[3,10],[5,10],[10],[1,20],[10]]

    param_2 = []  # Stores results of `find()`
    
    for i in range(len(method_call)):
        if method_call[i] == "find":
            param_2.append(obj.find(number_container[i][0]))  # Store the result of find()
        elif method_call[i] == "change":
            obj.change(number_container[i][0], number_container[i][1])  # No need to store
            param_2.append(None)
    print(param_2)  # Print only the results of `find()`
