class Node():
    def __init__(self, data):
        self.data = data
        self.nref = None
        self.pref = None

class linked_list():
    def __init__(self) :
        self.head = None
    
    def insert_empty(self, data):
        if self.head == None:
            node = Node(data)
            self.head = node
        else: 
            print ('linked list is not empty')
    
    def insert_beg(self, data):
        if self.head is None :
            node = Node(data)
            self.head = node
        else :    
            node = Node(data)
            node.nref = self.head
            self.head.pref = node
            self.head = node
        
    def insert_end(self, data):
        if self.head is None:
            node = Node(data)
            self.head = node
        
        else:
            node = Node(data)
            n = self.head
            while n.nref is not None :
                n = n.nref
            
            node.pref = n
            n.nref = node


    def insert_after(self, data, x):
        node = Node(data)
        if self.head is None:
            print('Linked list is empty')
        else:
            n = self.head
            while n is not None:
                if x == n.data:
                    break
                n = n.nref
            if n is None:
                print(f'{x} is not present in linked list')
            elif n.nref is None:
                n.nref = node
                node.pref = n
            else:
                n.nref.pref = node
                node.nref = n.nref
                n.nref = node
                node.pref = n

    def insert_before(self, data, x):
        node = Node(data)
        if self.head is None:
            print('Linked List is empty')
        else:
            n = self.head
            while n is not None:
                if x == n.data:
                    break
                n = n.nref
            if n is None:
                print(f'{x} is not present in the linked list')
            elif n.pref is None:
                node.nref = n
                n.pref = node
                self.head = node
            else:
                n.pref.nref = node
                node.pref = n.pref
                node.nref = n
                n.pref = node

    def print_LL(self):
        if self.head is None :
            print('Linked List is empty')
        else :
            n = self.head
            while n is not None :
                print(f'{n.data}-->',end="")
                n = n.nref

    def remove_beg(self):
        self.head.nref.pref = None
        self.head = self.head.nref 

    def remove_last(self):
        n = self.head
        while n.nref is not None:
            n = n.nref
        n.pref.nref = None
        n.pref = None
    
    def remove_after(self, x):
        if self.head is None:
            print('Linked list is empty')
        else :
            n = self.head 
            while n is not None:
                if x == n.data:
                    break
                n =n.nref
            if n is None:
                print(f'{x} is not present in Linked list')
            elif n.nref is None:
                print('Nothing to delete here')
            elif n.nref.nref is None:
                n.nref = None
            else:
                n.nref= n.nref.nref
                n.nref.pref = n

    def remove_before(self, x):
        if self.head is None:
            print('Linked list is empty')
        else:
            n = self.head
            while n is not None:
                if x ==  n.data:
                    break
                n = n.nref
            if n is None:
                print('Nothing to delete here')
            elif n == self.head:
                print('No value before head')
            elif n.pref == self.head :
                self.head = n
                n.pref = None
            else:
                n.pref = n.pref.pref
                n.pref.nref = n




ll1 = linked_list()
ll1.insert_empty(12)
ll1.insert_beg(34)
ll1.insert_end(87)
ll1.insert_after(45, 34)
ll1.insert_after(77, 87)
ll1.insert_end(100)
ll1.insert_after(1, 100)
ll1.insert_before(66, 77)
ll1.insert_before(44, 34)
# ll1.remove_beg()
# ll1.remove_last()
# ll1.remove_after(77)
# ll1.remove_before(34)
ll1.print_LL()
