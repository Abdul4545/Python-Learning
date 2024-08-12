# class Employee:
#     company = "Apple"
    
#     def __init__(self, name):
#         self.name = name
    
#     def show(self):
#         print(f"The name is {self.name} and company is {self.company}")
      
      

#     # def changeCompany(cls, newCompany):
#     #     cls.company = newCompany
    
#     # In the above method cls is behaving as self, that is not a class method  
    
#     @classmethod
#     def changeCompany(cls, newCompany):
#         cls.company = newCompany
 
        
# e1 = Employee("Abdul Moid")
# e1.show()
# e1.changeCompany("Tesla")
# e1.show()
# print(Employee.company)


# e2 = Employee("Abdul Moid")
# e2.show()
# # e2.changeCompany("Tesla")
# Employee.changeCompany("Tesla")
# e2.show()
# print(Employee.company)




# class method as an alternative constructor

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def fromStr(cls, string):
        return cls(string.split("-")[0], string.split("-")[1])
    
    

# e = Employee("Harry", 12000)
# print(e.name)
# print(e.salary)

string1 = "Moid-12000"
e1 = Employee(string1.split("-")[0], int(string1.split("-")[1]))

print(e1.name)
print(e1.salary)

string2 = "Asaad-23000"
e2 = Employee.fromStr(string2)
print(e2.name)
print(e2.salary)
