class Hash():
    def __init__(self):
        self.MAX = 100
        self.arr = [[] for i in range(self.MAX)]
    
    def hash_value(self, key):
        h=0
        for char in key :
            h = h + ord(char)
        return h% self.MAX
    
    def __getitem__(self, key):
        h = self.hash_value(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]

    def __setitem__(self, key, value):
        h = self.hash_value(key)
        found = False
        for index, element in enumerate(self.arr[h]):
            if len(element)==2 and element[0] == key:
                self.arr[h][index] = (key,value)
                found =  True
        if not found :
            self.arr[h].append((key,value))
    
    def __delitem__(self,key):
        h = self.hash_value(key)
        found = False
        for index, element in enumerate(self.arr[h]):
            if len(element)==2 and element[0]==key:
                del self.arr[h][index]
            found = True


h1 = Hash()
h1.__setitem__('march 45', 2700)
print(h1.__getitem__('march 45'))
h1.__delitem__('march 45')
print(h1.__getitem__('march 47'))