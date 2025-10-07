# In CLL the tail reference points to the head reference


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        

class CircularSLList:
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
    
    # Creation of circular singly linked list
    def createCSLL(self, nodeValue):
        node = Node(nodeValue)
        node.next = node
        self.head = node
        self.tail = node
        return "The CSLL has been created"
    
    # Insertion 
    def InsertCSLL(self, value, location):
        if self.head is None:
            return "The head reference is None"
        else:
            newNode = Node(value)
            if location == 0:
                newNode.next = self.head
                self.head = newNode
                self.tail.next = newNode
            elif location == 1:
                newNode.next = self.tail.next
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
            return "The node has been successfully inserted"
        
    # Searching for a node
    def searchCSLL(self, value):
        if self.head is None:
            return "There is not any node in this CSLL"
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == value:
                    return tempNode.value
                tempNode = tempNode.next
                if tempNode == self.tail.next:
                    return "The node does not exist in this CSLL"
        
        

        
                
                
                
    

clist = CircularSLList()
clist.createCSLL(1)
clist.InsertCSLL(0,0)
clist.InsertCSLL(2,1)
clist.InsertCSLL(4,1)
clist.InsertCSLL(5,1)
clist.InsertCSLL(3,3)

print(['->'.join([str(node.value) for node in clist])])
print(clist.searchCSLL(6))