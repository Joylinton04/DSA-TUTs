class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    

tree = TreeNode("Web development")
leftNode = TreeNode("Frontend")
rightNode = TreeNode("Backend")
leftNode1 = TreeNode("HTML")

tree.left = leftNode
tree.right = rightNode
leftNode.left = leftNode1

def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.value)
    preOrderTraversal(rootNode.left)
    preOrderTraversal(rootNode.right)


preOrderTraversal(tree)