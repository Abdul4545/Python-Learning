class A:
    def __init__(self):
        self.value = 'A'


class B(A):
    def __init__(self): 
        super().__init__() 
        self.value = 'B'


class C(A):
    def __init__(self): 
        super().__init__() 
        self.value = 'C'


class D(B, C):
    def __init__(self): 
        super().__init__()


obj = D() 
print(obj.value)
print(D.mro())

# [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]