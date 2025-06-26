# your task is to complete this function
# function should return new head pointer

'''
class node:
    def __init__(self):
        self.data = None
        self.next = None
'''

def deleteNode(head, x):
    if not head:
        return head
    temp = head
    if x==1:
        return head.next
    if x==2:
        head.next = head.next.next
        return head
        
    for _ in range(x-2):
        temp = temp.next
    
    temp.next = temp.next.next
        
    return head
    
        
    
