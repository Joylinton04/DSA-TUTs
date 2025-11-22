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

    

print("PreOrder Traversal:")
preOrderTraversal(tree)
print("\nInOrder Traversal:")
InOrderTraversal(tree)
print("\nPostOrder Traversal:")
postOrderTraversal(tree)
print("\nLevelOrder Traversal:")
levelOrderTraversalWithQueueLinkedList(tree)



print("\nSearching a node:")
print(searchNode(tree, "Backend dev"))