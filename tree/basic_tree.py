# Basic tree

class TreeNode:
    def __init__(self, data, children=[]):
        self.data = data
        self.children = children
        
    def __str__(self, level=0):
        ret = " " * level + str(self.data) + "\n"
        for child in self.children:
            ret += child.__str__(level+4)
        return ret
    
    def addChild(self,TreeNode):
        self.children.append(TreeNode)
        

tree = TreeNode("Web development", [])
frontend = TreeNode("Frontend dev", [])
backend = TreeNode("Backend dev", [])

frontend.addChild(TreeNode("HTML",[]))
backend.addChild(TreeNode("NODE JS",[]))

tree.addChild(frontend)
tree.addChild(backend)
print(tree)