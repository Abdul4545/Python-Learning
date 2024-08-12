class User:
    
    def __init__(self, name, id, age, pass_code):
        self.name = name
        self.id = id
        self.age = age
        self.pass_code = pass_code
        
    
    def login(self):
        print("Logged In")
        
     
    def _logout(self):
        print("Logged Out")
        
        
        
class Student(User):
    
    def __init__(self, name, id, marks, roll_no, age, pass_code):
        
        # self.name = name
        # self.id = id
        # self.age = age
        # self.pass_code = pass_code
        # self.marks = marks
        # self.roll_no = roll_no
        
        
        super().__init__(name, id, age, pass_code)
        self.marks = marks
        self.roll_no = roll_no
        
        
    def play(self):
        print("Playing")
        
    # def login(self):
    #     super().login()
    
    # def login(self):
    #     print("Logged in from child")
    
    def login(self):
        print("OTP verified successfully")
        super().login()
    
        
    def print_details(self):
        print(f"User name is {self.name} and id is {self.id}.")


# user1 = User()
# user1._logout()
 
 
# s1 = Student("Abdul Moid", 12867)
# s1.login()
# s1.print_details()
# s1._logout()


# name, id, marks, roll_no, age, pass_code
s1 = Student("Abdul Moid", 12867, 87.3, 12, 22, "123sdf")
print(s1.name, s1.id, s1.marks, s1.roll_no, s1.age, s1.pass_code)
s1.login()
s1.print_details()
s1._logout()