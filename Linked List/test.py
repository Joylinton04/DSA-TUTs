class Node():
    def __init__(self, value=None):
        self.value = value
        self.next = None


class SLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    def insertSLL(self, value, location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            elif location == 1:
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index =  0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
            
    def traverseSLL(self):
        if self.head is None:
            print("No data found")
            return
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next
    
    def searchSLL(self, value):
        if self.head is None:
            print("No data found")
            return
        else:
            node = self.head
            while node is not None:
                if node.value == value:
                    print(f"Data exists: {node.value}")
                    return
                node = node.next
            print("The value does not exist")
            return

        


node1 = Node(1)
node2 = Node(2)

linkedList = SLinkedList()
linkedList.insertSLL(1,0)
linkedList.insertSLL(2,1)
linkedList.insertSLL(4,1)
linkedList.insertSLL(3,2)

print([node.value for node in linkedList])
linkedList.traverseSLL()
linkedList.searchSLL(5)