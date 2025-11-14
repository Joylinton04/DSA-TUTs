# Queue using linkedlist

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
class Queue:
    def __init__(self):
        self.LinkedList = LinkedList()
    def __iter__(self):
        node = self.LinkedList.head
        while node:
            yield node
            node = node.next
            
    def isEmpty(self):
        if self.LinkedList.head == None:
            return True
        else:
            return False
    
    def enqueue(self, value):
        node = Node(value)
        if self.LinkedList.head is None:
            self.LinkedList.head = node
            self.LinkedList.tail = node
        else:
            self.LinkedList.tail.next = node
            self.LinkedList.tail = node
        
    def dequeue(self):
        if self.isEmpty():
            return "Queue is Empty"
        else:
            if self.LinkedList.head == self.LinkedList.tail:
                self.LinkedList.head = None
                self.LinkedList.tail = None
            else:
                self.LinkedList.head = self.LinkedList.head.next
    
    def peek(self):
        if self.isEmpty():
            return "Queue is Empty"
        else:
            return self.LinkedList.head.value
        
    def delete(self):
        self.LinkedList.head = None
        self.LinkedList.tail = None
    
    
customQueue = Queue()
customQueue.enqueue(1)
customQueue.enqueue(2)
print([node.value for node in customQueue])
customQueue.dequeue()
print([node.value for node in customQueue])
print(customQueue.peek())