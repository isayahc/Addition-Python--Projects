class Node:
    def __init__(self,data):
        self.data = data 
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None 

    def addNodeL(self, value):
        #self.root = Node(value) if not self.root else self.root.left = Node(value)
        if not self.root:
            self.root = Node(value)
        else:
            self.root.left = Node(value)

    def addNodeR(self, value):
        if not self.root:
            self.root = Node(value):
        else:
            self.root.right = Node(value)

    def MoveL(self):
        if self.left:

                


if __name__ == '__main__':
    
    x = Node(10)
    x.left = Node(20)
    x.right = Node (30)

    x.printt()

    