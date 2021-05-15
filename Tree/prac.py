class Node(object):
    def init(self, data):
        self.root = data
        self.left = None
        self.right = None

class BST(object):
    def init(self):
        self.top = None

    def recursBST(self, node, data):
        if node is None:
            node = Node(data)
        elif self.top.root > data:
            node.left = self.recursBST(node.left, data)
        elif  self.top.root < data:
            node.right = self.recursBST(node.right, data)

        return node

    def insert(self, data):
        self.top = self.recursBST(self.top, data)

conv = BST()
conv.insert(8)
conv.insert(3)
conv.insert(6)
conv.insert(1)
conv.insert(-1)
conv.insert(10)
conv.insert(14)
conv.insert(50)