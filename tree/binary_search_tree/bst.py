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
        


BST = BinarySearchTree()
BST.insert(10)
BST.insert(5)
BST.insert(15)
BST.insert(3)
BST.insert(7)
BST.insert(12)
BST.insert(20)