# Definition for singly-linked list. 
# 21. Merge two sorted lists in leet code


# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#         cur = dummy = ListNode()
#         while list1 and list2:               
#             if list1.val < list2.val:
#                 cur.next = list1
#                 list1, cur = list1.next, list1
#             else:
#                 cur.next = list2
#                 list2, cur = list2.next, list2
                
#         if list1 or list2:
#             cur.next = list1 if list1 else list2
            
#         return dummy.next
    
class ListNode:
    def __init__(self, val=0, next = None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def push(self, new_data):
        new_node = ListNode(new_data)
        new_node.next = self.head
        self.head = new_node
        # return new_node

    def insertAfter(self, prev_node, new_data):
        if prev_node is None:
            print("The given previous node doesn't exist.")
            return
        
        new_node = ListNode(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        

    def append(self, new_data):
        new_node = ListNode(new_data)
        if(self.head is None):
            self.head = new_node
            return
        else:
            last = self.head
            while (last.next):
                last = last.next

            last.next = new_node
        
        return self.head
    
    def printlist(self):
        temp = self.head
        while temp:
            print(temp.val, end=' ')
            temp = temp.next
        


if __name__ == "__main__":

    insert = LinkedList()

    insert.push(3)
    insert.push(8)
    insert.push(6)
    insert.push(5)
    insert.push(2)
    print(insert.printlist())
    insert.append(10)

    print(insert.printlist())

    # insert.insertAfter(8,11)
    # print(insert.printlist())
