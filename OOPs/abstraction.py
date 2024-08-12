from abc import ABC, abstractmethod

# abstract class 
class User(ABC):
    
    # def __init__(self):
    #     pass
    
    @abstractmethod
    def login(self):
        pass
    
    def logout(self):
        print("Logged out")
    
    
    @abstractmethod
    def auth(self):
        pass
    
    
class Buyer(User):
    
    def auth(self):
        return True
    
    def login(self):
        if(self.auth()):
            print("Logging in Buyer User")
        
    
    # def check_object(self, link):
    #     print(link)
 
 
class Seller(User):
    
    def auth(self):
        return True
    
    def login(self):
        if(self.auth()):
            print("Logging in seller User")
        
    
    # def check_object(self, link):
    #     print(link)       
        
b1 = Buyer()
b1.login()

s1 = Seller()
s1.login()


# Abstract classes are useful when we have a group of related objects that should share some common features but may or may not have different implementation

# helps in prepairing a blue print for other classes