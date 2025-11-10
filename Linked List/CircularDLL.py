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
                
    def traverseCDLL(self):
        if self.head is None:
            return "The CDLL is empty"
        else:
            tempNode = self.head
            while True:
                print(tempNode.value)
                if tempNode == self.tail:
                    break
                tempNode = tempNode.next
    
    def reverseTraverse(self):
        if self.head is None:
            return "The CDLL is empty"
        else:
            node = self.tail
            while node:
                print(node.value)
                if node == self.head:
                    break
                node = node.prev
    
    def searchCDLL(self, value):
        if self.head is None:
            return "The CDLL is empty"
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == value:
                    return tempNode.value
                if tempNode == self.tail:
                    return "The value does not exist"
                tempNode = tempNode.next
                
    def deleteNode(self, location):
        if self.head is None:
            return "The CDLL is empty"
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.prev = None
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = self.tail
                    self.head.next = self.head
            elif location == 1:
                if self.head == self.tail:
                    self.head.prev = None
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = self.head
                    self.head.prev = self.tail
            else:
                curNode = self.head
                index = 0
                while index < location - 1:
                    curNode = curNode.next
                    index += 1
                curNode.next = curNode.next.next
                curNode.next.prev = curNode
                print("The node has been successfully deleted")



    
ll = CircularDLL()

print([node.value for node in ll])
ll.createCDLL(2)
print([node.value for node in ll])
ll.insertCDLL(1,1)
ll.insertCDLL(0,1)
ll.insertCDLL(3,2)
print([node.value for node in ll])
ll.traverseCDLL()
print()
ll.reverseTraverse()