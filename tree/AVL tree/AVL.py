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
    
    def getHeight(self, rootNode):
        if not rootNode:
            return 0
        return rootNode.height
    
    def rotateRight(self, disbalancedNode):
        newRoot = disbalancedNode.left
        disbalancedNode.left = newRoot.right
        newRoot.right = disbalancedNode
        disbalancedNode.height = 1 + max(self.getHeight(disbalancedNode.left), self.getHeight(disbalancedNode.right))
        newRoot.height = 1 + max(self.getHeight(newRoot.left), self.getHeight(newRoot.right))
        return newRoot
    
    def rotateLeft(self, disbalancedNode):
        newRoot = disbalancedNode.right
        disbalancedNode.right = newRoot.left
        newRoot.left = disbalancedNode
        disbalancedNode.height = 1 + max(self.getHeight(disbalancedNode.left), self.getHeight(disbalancedNode.right))
        newRoot.height = 1 + max(self.getHeight(newRoot.left), self.getHeight(newRoot.right))
        return newRoot
    
    def getBalance(self, rootNode):
        if not rootNode:
            return 0
        return self.getHeight(rootNode.left) - self.getHeight(rootNode.right)
    
    def insertNode(self, rootNode, nodeValue):
        if not rootNode:
            return AVLNode(nodeValue)
        elif rootNode.data > nodeValue:
            rootNode.left = self.insertNode(rootNode.left, nodeValue)
        else:
            rootNode.right = self.insertNode(rootNode.right, nodeValue)

        rootNode.height = 1 + max(self.getHeight(rootNode.left), self.getHeight(rootNode.right))
        balance = self.getBalance(rootNode)
    
    # 4. If unbalanced, perform rotations
    
    # Case 1: Left-Left (Left heavy, inserted in left child's left)
    # Case 2: Left-Right (Left heavy, inserted in left child's right)
    # Case 3: Right-Right (Right heavy, inserted in right child's right)
    # Case 4: Right-Left (Right heavy, inserted in right child's left)

        if balance > 1 and nodeValue < rootNode.left.data:
            return self.rotateRight(rootNode)
        elif balance > 1 and nodeValue > rootNode.left.data:
            rootNode.left = self.rotateLeft(rootNode.left)
            return self.rotateRight(rootNode)
        elif balance < -1 and nodeValue > rootNode.right.data:
            return self.rotateLeft(rootNode)
        elif balance < -1 and nodeValue < rootNode.right.data:
            rootNode.right = self.rotateRight(rootNode.right)
            return self.rotateLeft(rootNode)
        return rootNode

    def getMinValueNode(rootNode):
        if rootNode is None or rootNode.left is None:
            return rootNode
        return getMinValueNode(rootNode.left)
            
            



newAVL = AVLTree()
rootNode = AVLNode(50)
rootNode = newAVL.insertNode(rootNode, 20)
rootNode = newAVL.insertNode(rootNode, 10)
rootNode = newAVL.insertNode(rootNode, 30)
rootNode = newAVL.insertNode(rootNode, 40)
rootNode = newAVL.insertNode(rootNode, 60)
rootNode = newAVL.insertNode(rootNode, 25)
print(rootNode.right.data)
# newAVL.levelOrderTraversal(rootNode)