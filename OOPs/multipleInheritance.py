class Father:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        return f"Name: {self.name}, Age: {self.age}"

    def speak(self):
        return "Father speaks carefully."


class Mother:

    def __init__(self, name, fav_food):
        self.name = name
        self.fav_food = fav_food

    def show_fav_food(self):
        return f"Favourite Food: {self.fav_food}"

    def speak(self):
        return "mother speaks lovingly"


class Child(Father, Mother):

    def __init__(self, name, age, fav_food, hobby):
        Father.__init__(self, name, age)
        Mother.__init__(self, name, fav_food)
        self.hobby = hobby

    def show_hobby(self):
        return f"Hobby: {self.hobby}"

    # def speak(self):
    #     return "mother speaks excitedly."



child = Child("Abdul Moid", 22, "Pizza", "Playing")

print(child.show_details())
print(child.show_fav_food())
print(child.show_hobby())
print(child.speak())


print(Child.mro())
