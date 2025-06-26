class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def insert_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
    
    def insert_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1
    
    def insert_at_index(self, index, data):
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds")
        
        if index == 0:
            self.insert_beginning(data)
            return
        
        new_node = Node(data)
        current = self.head
        for i in range(index - 1):
            current = current.next
        
        new_node.next = current.next
        current.next = new_node
        self.size += 1
    
    def delete_beginning(self):
        if not self.head:
            raise ValueError("List is empty")
        
        deleted_data = self.head.data
        self.head = self.head.next
        self.size -= 1
        return deleted_data
    
    def delete_end(self):
        if not self.head:
            raise ValueError("List is empty")
        
        if not self.head.next:
            deleted_data = self.head.data
            self.head = None
            self.size -= 1
            return deleted_data
        
        current = self.head
        while current.next.next:
            current = current.next
        
        deleted_data = current.next.data
        current.next = None
        self.size -= 1
        return deleted_data
    
    def delete_at_index(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        
        if index == 0:
            return self.delete_beginning()
        
        current = self.head
        for i in range(index - 1):
            current = current.next
        
        deleted_data = current.next.data
        current.next = current.next.next
        self.size -= 1
        return deleted_data
    
    def delete_value(self, value):
        if not self.head:
            raise ValueError("List is empty")
        
        if self.head.data == value:
            return self.delete_beginning()
        
        current = self.head
        while current.next:
            if current.next.data == value:
                deleted_data = current.next.data
                current.next = current.next.next
                self.size -= 1
                return deleted_data
            current = current.next
        
        raise ValueError(f"Value {value} not found in list")
