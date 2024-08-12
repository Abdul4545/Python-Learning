# is -> is compares exact location in memory

# The is keyword is used to test if two variables refer to the same object.

# == -> compares the value

x = ["apple", "banana", "cherry"]
y = x
# print(x is y)

# Test two objects that are equal, but not the same object:

x = ["apple", "banana", "cherry"]
y = ["apple", "banana", "cherry"]
# print(x is y)
print(x == y)


a = 4
b = "4"
print(a == b)
print(a is b)


a = 3
b = 3
print(a == b)
print(a is b)