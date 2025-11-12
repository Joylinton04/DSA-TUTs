

class Node:
    def __init__(self, value):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
    

class Stack:
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
    
    def push(self, value):
        node = Node(value)
        node.next = self.LinkedList.head
        self.LinkedList.head = node
    
    def pop(self):
        if self.isEmpty():
            return "The stack is empty"
        else:
            value = self.LinkedList.head.value
            self.LinkedList.head = self.LinkedList.head.next
            return value
    
    def peek(self):
        if self.isEmpty():
            return "The stack is empty"
        else:
            return self.LinkedList.head.value
    
    def delete(self):
        self.LinkedList.head = None
        
    
customStack = Stack()
customStack.push(1)
customStack.push(2)
customStack.push(3)
print([node.value for node in customStack])
print(customStack.isEmpty())
print("Pop")
print(customStack.pop())
print("Peek")
print(customStack.peek())