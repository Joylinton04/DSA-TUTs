class AVLNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def __init__(self):
        self.root = None

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



newAVL = AVLTree()
newAVL.levelOrderTraversal(newAVL.root)