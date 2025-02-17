class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None
    def __int__(self) -> int:
        return int(self.data)

class Solution:
    def insert(self, head, data):
        node = Node(data)
        if head is None:
            head = node
        elif head.next is None:
            head.next = node
        else:
            start = head
            while start.next:
                start = start.next
            start.next = node
        return head
    
    def display(self, head):
        cur = head
        while cur:
            print(cur.data, end=' ')
            cur = cur.next

    def removeDuplicates(self,head):
        if head is None:
            return
        cur = head
        next = None
        while cur.next is not None:
            if cur.data == cur.next.data:
               next = cur.next.next
               cur.next  = next
            else:
                cur = cur.next
        return head
    
T = int(input())
head = None
myList = Solution()
for i in range(T):
    data = int(input())
    head = myList.insert(head, data)

# myList.display(head)
head = myList.removeDuplicates(head)
myList.display(head)
                    
                    
                


    