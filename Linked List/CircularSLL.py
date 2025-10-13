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
                
    # Traversing the CSLL
    def travseringCSLL(self):
        if self.head is None:
            print("The CSLL does not exist")
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next
                if tempNode == self.tail.next:
                    break
                
    # Deletion of a node
    def deleteNode(self, location):
        if self.head is None:
            print("CSLL does not exist")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.tail.next = self.head
            elif location == 1:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    index = 0
                    while node is not None:
                        if node.next == self.tail:
                           break 
                        node = node.next
                    node.next = self.head
                    self.tail = node
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next
    
        # Deletion of CSLL
    def deleteCSLL(self):
        self.head = None
        self.tail.next = None
        self.tail = None
    

clist = CircularSLList()
clist.createCSLL(1)
clist.InsertCSLL(0,0)
clist.InsertCSLL(2,1)
clist.InsertCSLL(4,1)
clist.InsertCSLL(5,1)
clist.InsertCSLL(3,3)

print([node.value for node in clist])
# print(clist.searchCSLL(6))

# clist.travseringCSLL()

# clist.deleteNode(0)
clist.deleteNode(1)
clist.InsertCSLL(6, 1)
clist.InsertCSLL(7, 1)


print([node.value for node in clist])

# clist.deleteCSLL()

# print([node.value for node in clist])