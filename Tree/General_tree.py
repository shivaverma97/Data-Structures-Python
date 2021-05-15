class Treenode():
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
    
    def add_node(self, child):
        self.children.append(child)
        child.parent = self

    def get_level(self):
        level = 0 
        p = self.parent
        while p :
            level = level+1
            p = p.parent

        return level


    def print_tree(self):
        level = self.get_level()
        Prefix = "   "*level + '-->' if self.parent else ""
        print(f'{Prefix}{self.data}')
        if len(self.children) > 0 :
            for child in self.children:
                child.print_tree()


def build_tree():
    root = Treenode('Electronics')
    
    laptop = Treenode('Laptop')
    root.add_node(laptop)
    laptop.add_node(Treenode('ASUS'))
    laptop.add_node(Treenode('Acer'))
    laptop.add_node(Treenode('Lenovo'))

    Phone = Treenode('Phone')
    root.add_node(Phone)
    Phone.add_node(Treenode('Samsung'))
    Phone.add_node(Treenode('iPhone'))
    Phone.add_node(Treenode('Mi'))

    TV = Treenode('TV')
    root.add_node(TV)
    TV.add_node(Treenode('Sony'))
    TV.add_node(Treenode('LG'))
    TV.add_node(Treenode('OnePlus'))

    root.print_tree()
    
    return root

if __name__ == '__main__':
    root = build_tree()
    