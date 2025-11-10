
class Stack:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.list = []
    def __str__(self):
        if self.list == []:
            return "Stack is Empty"
        else:
            values = self.list.reverse()
            values = [str(x) for x in self.list]
            return '\n'.join(values)
    
    # isEmpty
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
        
    def isFull(self):
        if len(self.list) == self.maxSize:
            return True
        else:
            return False

    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
    
    def push(self,value):
        if self.isFull():
            return "Stack is full"
        else:
            self.list.append(value)
            return "The element has been successfully inserted"
    
    # pop
    def pop(self):
        if self.isEmpty():
            return "Stack is Empty"
        else: 
            self.list.pop()
    
    # peek
    def peek(self):
        if self.isEmpty():
            return "Stack is Empty"
        else: 
            return self.list[len(self.list)-1]
        
    # delete
    def delete(self):
        self.list.clear()
        
    

customStack = Stack(3)
print(customStack.isFull())
print(customStack.push(1))
print(customStack.push(2))
print(customStack.push(3))
print(customStack.push(4))
print(customStack)
customStack.delete()
print(customStack)