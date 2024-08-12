class Student:
    
    # default constructor
    # here self is the object that is created
    # def __init__(self):
    #     # print(id(self))
    #     # print("I will be called automatically when you will create an object")
    #     self.name = "Moid"
    #     self.rollNo = 1
    #     self.marks = 85.8
    
    
    __numberOfStudents = 0
    __schoolName = "SPS"
    
    def __init__(self, name, rollNo, marks):
        
        # print(id(self))
        # print("I will be called automatically when you will create an object")
        
        self.name = name
        self.rollNo = rollNo # public
        self.__marks = marks # private
        
        self.__numberOfStudents = Student.__numberOfStudents + 1
        
        Student.__numberOfStudents = Student.__numberOfStudents + 1
        
    def study(self):
        # print("I am " + self.name + " and I am studying")
        print(f"I am {self.name} and my roll number is {self.rollNo} and I am studying.")
        
    def play(self):
        print("I am " + self.name + " and I am playing")
    
    
    # private method
    def __auth(self):
        return "0000"
            
     
    #  getter   
    def get_mark(self):
        return self.__marks
    
    # setter
    def set_mark(self, new_mark, pass_code):
        if(pass_code == self.__auth()): # security for changing value
            self.__marks = new_mark
            
        else:
            return "Bhag jaao yahan se"
     
     
    @staticmethod
    def get_student_count():
        return Student.__numberOfStudents   
    
    
    @staticmethod
    def get_school_name():
        return Student.__schoolName  
    
    @staticmethod
    def set_school_name(new_school_name):
        Student.__schoolName = new_school_name 
    

# object of class
# s1 = Student()
# print("s1 is is ", id(s1))
# print(s1.name)
# print(s1.rollNo)
# print(s1.marks)


# s2 = Student()
# print("s2 is is ",  id(s2))
# print(s2.name)
# print(s2.rollNo)
# print(s2.marks)


s1 = Student("Moid", 1, 85.5)
print("s1 id is", id(s1))
print(s1.name)
print(s1.rollNo)
print(s1.get_mark())
s1.set_mark(86, "0000")
print(Student.get_school_name())
print("Updated mark is",s1.get_mark())

print(Student.set_school_name("Siddharth Public School"))
print(Student.get_school_name())



# s1.study()
# print(s1.numberOfStudents)

# print()

# s2 = Student("Asaad", 10, 95.5)
# print("s2 is is", id(s1))
# print(s2.name)
# print(s2.rollNo)
# print(s2.marks)
# s2.play()
# print(s2.numberOfStudents)
# print(Student.numberOfStudents)
# print(Student.schoolName)


# print(dir(Student))

# print(s1.__dict__)

# print(s1.__dict__)

print(help(Student))
# print(help(s1))