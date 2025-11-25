from QueueLinkedList import Queue

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    

tree = TreeNode("Web development")
leftNode = TreeNode("Frontend")
rightNode = TreeNode("Backend")
leftNode1 = TreeNode("HTML")
rightNode1 = TreeNode("Node JS")

tree.left = leftNode
tree.right = rightNode
leftNode.left = leftNode1
rightNode.left = rightNode1

def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.value)
    preOrderTraversal(rootNode.left)
    preOrderTraversal(rootNode.right)


def InOrderTraversal(rootNode):
    if not rootNode:
        return
    InOrderTraversal(rootNode.left)
    print(rootNode.value)
    InOrderTraversal(rootNode.right)
    

def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.left)
    postOrderTraversal(rootNode.right)
    print(rootNode.value)
    

def levelOrderTraversalWithList(rootNode):
    if not rootNode:
        return
    queue = []
    queue.append(rootNode)
    while queue:
        currentNode = queue.pop(0)
        print(currentNode.value)
        if currentNode.left:
            queue.append(currentNode.left)
        if currentNode.right:
            queue.append(currentNode.right)
    
def levelOrderTraversalWithQueueLinkedList(rootNode):
    if not rootNode:
        return 
    customQueue = Queue()
    customQueue.enqueue(rootNode)
    while not(customQueue.isEmpty()):
        root = customQueue.dequeue()
        print(root.value)
        if root.left is not None:
            customQueue.enqueue(root.left)
        if root.right is not None:
            customQueue.enqueue(root.right)
            
            

def searchNode(rootNode, nodeValue):
    if not rootNode:
        return "The binary tree is empty"
    customQueue = Queue()
    customQueue.enqueue(rootNode)
    while not(customQueue.isEmpty()):
        currentNode = customQueue.dequeue()
        if currentNode.value == nodeValue:
            return "The value exists in the binary tree"
        if currentNode.value == nodeValue:
            return "The value exists in the binary tree"
        if currentNode.left:
            customQueue.enqueue(currentNode.left)
        if currentNode.right:
            customQueue.enqueue(currentNode.right)
    return "The value does not exist in the binary tree"


def insertNodeBinaryTree(rootNode, newNode):
    if not rootNode:
        rootNode = newNode
        return
    customQueue = Queue()
    customQueue.enqueue(rootNode)
    while not(customQueue.isEmpty()):
        currentNode = customQueue.dequeue()
        if not currentNode.left:
            currentNode.left = newNode
            return
        else:
            customQueue.enqueue(currentNode.left)
        if not currentNode.right:
            currentNode.right = newNode
            return
        else:
            customQueue.enqueue(currentNode.right)
            


def getDeepestNode(rootNode):
    if not rootNode:
        return 
    customQueue = Queue()
    customQueue.enqueue(rootNode)
    while not(customQueue.isEmpty()):
        currentNode = customQueue.dequeue()
        if currentNode.left:
            customQueue.enqueue(currentNode.left)
        if currentNode.right:
            customQueue.enqueue(currentNode.right)
    deepestNode = currentNode
    return deepestNode.value


def deleteDeepestNode(rootNode, dNode):
    if not rootNode:
        return
    customQueue = Queue()
    customQueue.enqueue(rootNode)
    while not(customQueue.isEmpty()):
        currentNode = customQueue.dequeue()
        if currentNode.value is dNode:
            currentNode.value = None
            return
        if currentNode.right:
            if currentNode.right is dNode:
                currentNode.right = None
                return
            else:
                customQueue.enqueue(currentNode.right)
        if currentNode.left:
            if currentNode.left is dNode:
                currentNode.left = None
                return
            else:
                customQueue.enqueue(currentNode.left)
                
    
def deleteNode(rootNode, node):
    if not rootNode:
        return "The binary tree is empty"
    customQueue = Queue()
    customQueue.enqueue(rootNode)
    while not(customQueue.isEmpty()):
        currentNode = customQueue.dequeue()
        if currentNode.value == node:
            dNode = getDeepestNode(rootNode)
            currentNode.value = dNode
            deleteDeepestNode(rootNode, dNode)
            return "The node has been successfully deleted"
        if currentNode.left:
            customQueue.enqueue(currentNode.left)
        if currentNode.right:
            customQueue.enqueue(currentNode.right)
    return "Failed to delete the node"

    
    
def deleteBT(rootNode):
    rootNode.value = None
    rootNode.left = None
    rootNode.right = None
    return "Binary tree deleted successfully"







print("PreOrder Traversal:")
print("---------------")
preOrderTraversal(tree)
print("\nInOrder Traversal:")
print("---------------")
InOrderTraversal(tree)
print("\nPostOrder Traversal:")
print("---------------")
postOrderTraversal(tree)
print("\nLevelOrder Traversal:")
print("---------------")
levelOrderTraversalWithQueueLinkedList(tree)



print("\nSearching a node:")
print("---------------")
print(searchNode(tree, "Backend dev"))

print("\nDelete node:")
print("---------------")

print(deleteNode(tree, "Frontend"))

print("---------------")
levelOrderTraversalWithQueueLinkedList(tree)


print("---------------")
print(deleteBT(tree))
print("---------------")
levelOrderTraversalWithQueueLinkedList(tree)  