class Node:
    def __init__(self,value):
        self.value = value
        self.prev = None
        self.next = None


class CircularDLL:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            if node.next == self.head:
                break
            node = node.next
    
    def createCDLL(self, value):
        node = Node(value)
        self.head = node
        self.tail = node
        node.next = node
        node.prev = node
        return "The CDLL is created successfully"
    
    def insertCDLL(self,value,location):
        if self.head is None:
            return "The CDLL is empty"
        else: 
            node = Node(value)
            if location == 0:
                if self.head == self.tail:
                    node.next = node
                    node.prev = node
                    self.head = node
                    self.tail = node
                else:
                    node.next = self.head
                    node.prev = self.tail
                    self.head.prev = node
                    self.head = node
                    self.tail.next = node
            elif location == 1:
                node.next = self.head
                node.prev = self.tail
                self.head.prev = node
                self.tail.next = node
                self.tail = node
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                node.next = tempNode.next
                node.prev = tempNode
                node.next.prev = tempNode
                tempNode.next = node
                
                
    
ll = CircularDLL()

print([node.value for node in ll])
ll.createCDLL(2)
print([node.value for node in ll])
ll.insertCDLL(1,1)
ll.insertCDLL(0,1)
ll.insertCDLL(3,0)
print([node.value for node in ll])