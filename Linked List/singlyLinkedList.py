# create a head and tail, initialize with null
# create a blank node and assign a value to it and reference to null
# Link head and tail with this node

class Node():
    def __init__(self,value=None):
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
                newNode.next = self.tail
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head


SingkyLinkedList = SLinkedList()
print(node.value for node in SingkyLinkedList)
# SinglyLinkedList.head = node1
# SinglyLinkedList.head.next = node2
# SinglyLinkedList.tail = node2