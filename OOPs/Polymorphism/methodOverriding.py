class Animal:
    def sound(self):
        return "Some sound"
    
class Dog(Animal):
    # Overriding
    def sound(self):
        return "Barks"


animal = Animal()
print(animal.sound())

    
obj =  Dog()
print(obj.sound())