class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, nodeValue):
        if self.root is None:
            self.root = BSTNode(nodeValue)
        else:
            self._insert(nodeValue, self.root)
        return "Value Inserted"

    def _insert(self, nodeValue, currentNode):
        if nodeValue <= currentNode.data:
            if currentNode.left is None:
                currentNode.left = BSTNode(nodeValue)
            else:
                self._insert(nodeValue, currentNode.left)
        else:
            if currentNode.right is None:
                currentNode.right = BSTNode(nodeValue)
            else:
                self._insert(nodeValue, currentNode.right)
        return "Value Inserted"
        
    def preOrderTraversal(self, rootNode):
        if not rootNode:
            return
        print(rootNode.data)
        self.preOrderTraversal(rootNode.left)
        self.preOrderTraversal(rootNode.right)

    def inOrderTraversal(self, rootNode):
        if not rootNode:
            return
        self.inOrderTraversal(rootNode.left)
        print(rootNode.data)
        self.inOrderTraversal(rootNode.right)

    def postOrderTraversal(self, rootNode):
        if not rootNode:
            return
        self.postOrderTraversal(rootNode.left)
        self.postOrderTraversal(rootNode.right)
        print(rootNode.data)

    def levelOrderTraversal(self, rootNode):
        if not rootNode:
            return
        queue = []
        queue.append(rootNode)
        while queue:
            currentNode = queue.pop(0)
            print(currentNode.data)
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)

    def search(self, rootNode, nodeValue):
        if not rootNode:
            return "Value Not Found"
        if rootNode.data == nodeValue:
            return "Value Found"
        if nodeValue < rootNode.data:
            return self.search(rootNode.left, nodeValue)
        return self.search(rootNode.right, nodeValue)

    def minValueNode(self, currentNode):
        while currentNode.left is not None:
            currentNode = currentNode.left
        return currentNode

    def deleteNode(self, rootNode, nodeValue):
        if not rootNode:
            return rootNode
        if nodeValue < rootNode.data:
            rootNode.left = self.deleteNode(rootNode.left, nodeValue)
        elif nodeValue > rootNode.data:
            rootNode.right = self.deleteNode(rootNode.right, nodeValue)
        else:
            if rootNode.left is None:
                temp = rootNode.right
                rootNode = None
                return temp
            elif rootNode.right is None:
                temp = rootNode.left
                rootNode = None
                return temp
            temp = self.minValueNode(rootNode.right)
            rootNode.data = temp.data
            rootNode.right = self.deleteNode(rootNode.right, temp.data)
        return rootNode

    def delete(self, nodeValue):
        self.deleteNode(self.root, nodeValue)


BST = BinarySearchTree()
BST.insert(10)
BST.insert(5)
BST.insert(15)
BST.insert(3)
BST.insert(7)
BST.insert(12)
BST.insert(20)

print("Pre Order Traversal")
BST.preOrderTraversal(BST.root)

print("In Order Traversal")
BST.inOrderTraversal(BST.root)

print("Post Order Traversal")
BST.postOrderTraversal(BST.root)

print("Level Order Traversal")
BST.levelOrderTraversal(BST.root)