
class LBinaryT:
    def __init__(self, size):
        self.maxSize = size
        self.customList = size*[None]
        self.lastUsedIndex = 0

    def insertNode(self,value):
        if self.lastUsedIndex+1 == self.maxSize:
            return "The binary tree is full"
        self.customList[self.lastUsedIndex+1] = value
        self.lastUsedIndex += 1 
        return "Node inserted"
    
    def searchNode(self, value):
        for i in range(len(self.customList)):
            if self.customList[i] == value:
                return "Value found"
        return "Not Found"
    
    def preOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return
        print(self.customList[index])
        self.preOrderTraversal(index*2)
        self.preOrderTraversal(index*2+1)
        
    def inOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return
        self.inOrderTraversal(index*2)
        print(self.customList[index])
        self.inOrderTraversal(index*2+1)
        
    def postOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return
        self.postOrderTraversal(index*2)
        self.postOrderTraversal(index*2+1)
        print(self.customList[index])
        
        
    def levelOrderTraversal(self, index):
        for i in range(index, self.lastUsedIndex+1):
            print(self.customList[i])
            
    def deleteNode(self, value,index=1):
        if self.lastUsedIndex == 0:
            return "There is  no node to delete  "
        deepestNode = self.customList[self.lastUsedIndex]
        for i in range(index,self.lastUsedIndex+1):
            if self.customList[i] == value:
                self.customList[i] = deepestNode
                self.customList[self.lastUsedIndex] = None
                self.lastUsedIndex -= 1
                return "Node deleted"
            
    def deleteBinaryT(self):
        self.customList = None
        return "Binary tree deleted"
    
    
    

listBT = LBinaryT(8)
print(listBT.insertNode("Drinks"))
print(listBT.insertNode("Hot"))
print(listBT.insertNode("Cold"))
print(listBT.insertNode("Tea"))
print(listBT.insertNode("Coffee"))

print("\n--------------")
print(listBT.searchNode("Coffee"))
print("\n--------------")
print("PreOrder Traversal")
listBT.preOrderTraversal(1)
print("\n--------------")
print("InOrder Traversal")
listBT.inOrderTraversal(1)
print("\n--------------")
print("PostOrder Traversal")
listBT.postOrderTraversal(1)
print("\n--------------")
print("levelOrder Traversal")
listBT.levelOrderTraversal(1)
print("\n--------------")
print("Delete Node")
print("--------------")
print(listBT.deleteNode("Coffee"))
print("\n--------------")
print("levelOrder Traversal")
print("--------------")
listBT.levelOrderTraversal(1)