from LinkedList import LinkedList

def removeDups(ll):
    if ll.head is None:
        return
    else:
        currentNode = ll.head
        visited = set([currentNode.value])
        while currentNode.next:
            if currentNode.next.value in visited:
                currentNode.next = currentNode.next.next
            else:
                visited.add(currentNode.next.value)
                currentNode = currentNode.next
        return ll
    

def removeDups2(ll):
    if ll.head is None:
        return
    else:
        currentNode = ll.head
        while currentNode:
            runner = currentNode
            while runner.next:
                if runner.next.value == currentNode.value:
                    runner.next = runner.next.next
                else:
                    runner = runner.next
            currentNode = currentNode.next
        return ll.head

    
    
LL = LinkedList()
# LL.generate(10,0,99)
# print(LL)
# removeDups(LL)
# print(LL)

LL.add(1)
LL.add(1)
LL.add(2)
LL.add(3)
LL.add(4)
LL.add(4)
LL.add(5)
print(LL)

removeDups2(LL)
print(LL)