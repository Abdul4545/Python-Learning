# already did in complexClass

class Vector:
    
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k
        
    
    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"
    
    def __add__(self, x):
        return Vector(self.i + x.i, self.j + x.j , self.k + x.k)
    
    def __sub__(self, x):
        return Vector(self.i - x.i, self.j - x.j , self.k - x.k)
    
v1 = Vector(1,2,3)
print(f"v1 is {v1}")

v2 = Vector(2,3,4)
print(f"v2 is {v2}")

v3 = v1 + v2
print(f"v3 is {v3}")
print(type(v3))

v4 = v2 - v1
print(f"v4 is {v4}")