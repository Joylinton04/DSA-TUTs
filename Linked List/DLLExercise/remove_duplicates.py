from LinkedList import LinkedList

def removeDup(ll):
    if ll.head is None:
        return
    else:
        currentNode = ll.head
        while currentNode:
            tempNode = currentNode
            while tempNode.next:
                if currentNode.value == tempNode.next.value:
                    tempNode.next = tempNode.next.next
                else:
                    tempNode = tempNode.next
            currentNode = currentNode.next
        return ll
        
            
ll = LinkedList()
ll.generate(5,0,9)
print(ll)

print(removeDup(ll))