# Circular queue
# if enqueuing top pointer pointer is updated
# if dequeuing start pointer pointer is updated

class Queue:
    def __init__(self, maxSize):
        self.items = maxSize*[None]
        self.maxSize = maxSize
        self.start = -1
        self.top = -1
        
    def __str__(self):
        # if self.items == []:
        #     return "Queue is empty"
        # else:
        values = [str(x) for x in self.items]
        return ' -> '.join(values)
    
    def isFull(self):
        if self.top + 1 == self.start:
            return True
        elif self.start == 0 and self.top + 1 == self.maxSize:
            return True
        else:
            return False
        
    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False
        
    def enqueue(self,value):
        if self.isFull():
            print("The queue is full")
            return
        else:
            if self.top + 1 == self.maxSize:
                self.top = 0
            else:
                self.top += 1
                if self.start == -1:
                    self.start = 0
            self.items[self.top] = value
            
    def dequeue(self):
        if self.isEmpty():
            return "Queue is Empty"
        else:
            start = self.start
            if self.start == self.top:
                self.start = -1
                self.top = -1
            elif self.start + 1 == self.maxSize:
                self.start = 0
            else:
                self.start += 1
        self.items[start] =  None
        
    def peek(self):
        if self.isEmpty():
            return "Queue is Empty"
        else:
            return self.items[self.start]
            
    def delete(self):
        self.items = self.maxSize * [None]
        self.start = -1
        self.stop = -1
    
    
    
customQueue = Queue(4)
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
customQueue.enqueue(4)
print(customQueue)
print(customQueue.isFull())
customQueue.dequeue()
print(customQueue)
customQueue.dequeue()
print(customQueue)
customQueue.dequeue()
print(customQueue)
print(customQueue.peek())