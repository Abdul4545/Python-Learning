# print(1+1)
# print("1" + "1")
# print([1,2,3,4] + [5,6,7,8])

# the above examples are example of polymorphism


"""

In python we achieve polymorphism by
1) Method Overriding
2) Method Overloading
3) Operator Overloading

"""

# Method Overloading
# def sum(a, b):
#     return a + b

# print(sum(2,3))

# def sum(a, b, c):
#     return a + b + c

# print(sum(2,3,4))

# print(sum(2,3))

# the above method is not correct in python


# def sum1(a, b):
#     return a + b

# def sum2(a, b, c):
#     return a + b + c


# it is method overloading
# def betterSum(a, b, c=0):
#     if(c == 0):
#         return sum1(a,b)
        
#     else:
#         return sum2(a,b,c)


# print(betterSum(12, 13))
# print(betterSum(12, 13, 14))


# real life example of overloading
class User:
    
    def __init__(self, name, mobile_number, address = ""):
        if(address == ""):
            self.C1(name, mobile_number)
            
        else:
            self.C2(name, mobile_number, address)
     
        
    def C1(self, name, mobile_number):
        self.name = name
        self.mobile_number = mobile_number

    def C2(self, name, mobile_number, address):
        self.name = name
        self.mobile_number = mobile_number
        self.address = address



u1 = User("Moid", "8765445678")
print(u1.name)
print(u1.mobile_number)

print()

u2 = User("Asaad", "8765123465", "India")
print(u2.name)
print(u2.mobile_number)
print(u2.address)