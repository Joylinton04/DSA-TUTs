class heap:
    def __init__(self, size):
        self.customList = size*[None]
        self.heapSize = 0
        self.maxSize = size + 1

    def peakOfHeap(self, rootNode):
        if not rootNode:
            return
        else:
            return self.customList[1]

    def sizeOfHeap(self, rootNode):
        if not rootNode:
            return
        else:
            return rootNode.heapSize


    def levelOrderTraversal(self, rootNode):
        if not rootNode:
            return
        else:
            for i in range(1, rootNode.heapSize+1):
                print(self.customList[i])



bheap = heap(5)

# bheap.levelOrderTraversal()
print(bheap.sizeOfHeap(bheap))