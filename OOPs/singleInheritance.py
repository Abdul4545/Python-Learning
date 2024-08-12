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


father = Father("Abdul Moid", 22, "Engineer")
print(father.show_details())
print(father.show_occupation())
print(father.speak())
