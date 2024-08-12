class Grandfather:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        return f"Name: {self.name}, Age: {self.age}"

    def speak(self):
        return "Grandfather speaks wisely."


class Father(Grandfather):

    def __init__(self, name, age, occupation):
        super().__init__(name, age)
        self.occupation = occupation

    def show_occupation(self):
        return f"Occupation: {self.occupation}"

    def speak(self):
        return "Father speaks carefully"
    

class Uncle(Grandfather):

    def __init__(self, name, age, occupation):
        super().__init__(name, age)
        self.occupation = occupation

    def show_occupation(self):
        return f"Occupation: {self.occupation}"

    def speak(self):
        return "Uncle speaks harshly and loudly"
    
    
father = Father("Abdul Moid", 36, "Engineer")
print(father.show_details())
print(father.show_occupation())
print(father.speak())

print()

uncle = Uncle("Asaad", 26, "Doctor")
print(uncle.show_details())
print(uncle.show_occupation())
print(uncle.speak())

