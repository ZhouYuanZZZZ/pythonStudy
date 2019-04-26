class A:
    def __init__(self):
        self.size = 0

    def getSize(self):
        print("getter")
        return self.size + 666

    def setSize(self, size):
        print("setter")
        self.size = 10

    sizeProperty = property(getSize, setSize, None, '测试约束')


a = A()
a.sizeProperty = 123
print(a.sizeProperty)
