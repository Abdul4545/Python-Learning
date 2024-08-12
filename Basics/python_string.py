# name = "Moid"
# asaad = 'asaad'
# print(name + asaad)

string = "Hey my name is {} and I am from {}"
name = "Abdul Moid"
country = "India"

# print(string.format(name, country))

print(f"Hey my name is {name} and I am from {country}.")

txt = "For only{price: .2f} dollars."
print(txt.format(price = 23.3456))

# apple1 = "He said, \"I want to eat apple\""
apple2 = 'He said, "I want to eat apple"'
# print(apple1)
# print(apple2)


newLine = """Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.
It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.
It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."""

# print(newLine)

# printing each character of string
# for ch in apple2:
#     print(ch)




# string slicing

str = "abdulMoid" 

# print(len(str))
# print(str[2:5])
# 5th index is excluded

# print(str[:5])
# print(str[-1:0])
# it is similar to len(str)-1 : 0 ---> 8:0

# print(str[-4:-2])
# print(str[len(str)-4: len(str)-2])


# strings are immutable
# string methods
print(str.upper())
print(str)
print(str.lower())

str2 = "!!!! asdf werf edf!!!!!!!!!!!!!"
str3 = str2.rstrip("!") 
# strips only trailing
print(str3)

print(str2.replace("!", "a"))

print(str2.split(" "))
# makes a list

print(str.capitalize())
# converts 1st character to upparcase else all to lowercase

# print(str.center(30))
# print(str.center(30, "."))

# print(apple2.count("a"))

# print(str2.endswith("!!!!!"))

# print(apple2.endswith("want", 2, 16))

# print(apple2.find("want"))

string = "asdfg@1"
string2 = "asdfg1234"
string3 = "asdfgASDGHJ"
# print(string.isalnum())
# print(string2.isalnum())
# print(string3.isalpha())

print(string.islower())
# A string is lowercase if all cased characters in the string are lowercase and there is at least one cased character in the string.

string4 = "hello\n"

# print(string3.isprintable())
# print(string4.isprintable())

string5 = "      "
string6 = "hel lo "

# print(string5.isspace())
# print(string6.isspace())

title1 = "Hello How"
title2 = "hello how"

# print(title1.istitle())
# print(title2.istitle())

# print(title2.title())


# docstrings
# python docstring are the string literals that appear right after the definition of a function, method, class or module

def square(n):
    '''takes in a number n, prints the square of n'''
    print(n**2)
    
square(5)

print(square.__doc__)
