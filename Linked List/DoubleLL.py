class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None
        

class DoubleLList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    
    def createDLL(self, value):
        node = Node(value)
        self.head = node
        self.tail = node
        node.next = None
        node.prev = None
        return "The DLL has been created"
    
    def insertDLL(self,value,location):
        if self.head == None:
            print("This node cannot be inserted")
        else:
            newNode = Node(value)
            if location == 0:
                newNode.prev = None
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode
            elif location == 1:
                newNode.next = None
                newNode.prev = self.tail
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                newNode.next = tempNode.next
                newNode.prev = tempNode
                newNode.next.prev = newNode
                tempNode.next = newNode
                
    def traverseDLL(self):
        if self.head is None:
            print("There are no nodes in DLL")
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next
                
    def reverseTraverse(self):
        if self.head is None:
            print("There are no nodes in DLL")
        else:
            tempNode = self.tail
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.prev
    
    def searchDLL(self,value):
        if self.head is None:
            print("There are no nodes in DLL")
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == value:
                    return tempNode.value
                tempNode = tempNode.next
            return "The node does not exist in this list"
        
    def deleteNode(self, location):
        if self.head == None:
            print("There are no nodes in DLL")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.next = None
                    self.head.prev = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = None
            elif location == 1:
                if self.head == self.tail:
                    self.head.next = None
                    self.head.prev = None
                    self.head = None
                    self.tail = None
                else: 
                    self.tail = self.tail.prev
                    self.tail.next = None
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                tempNode.next = tempNode.next.next
                tempNode.next.prev = tempNode
    
    def deleteDLL(self):
        if self.head is None:
            return "There are no nodes in DLL"
        else:
            tempNode = self.head
            while tempNode:
                tempNode.prev = None
                tempNode = tempNode.next
            self.head = None
            self.tail = None
            print("DLL has been deleted")
                    
    
Dll = DoubleLList()
print(Dll.createDLL(5))
print([node.value for node in Dll])
Dll.insertDLL(4,0)
# Dll.insertDLL(3,0)
Dll.insertDLL(2,0)
Dll.insertDLL(1,0)
Dll.insertDLL(6,1)
Dll.insertDLL(3,2)
print([node.value for node in Dll])

# Dll.traverseDLL()
# print("\nReverse Traverse\n")
# Dll.reverseTraverse()

# print(Dll.searchDLL(5))
Dll.deleteNode(1)
print([node.value for node in Dll])
Dll.deleteDLL()
Dll.traverseDLL()