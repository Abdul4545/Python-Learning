def hello():
    print("hello")
    
# hello()
# hello()


def returns():
    return 1

# print(returns())
# print(returns())


# will write the code of this function later
def baad():
    pass


# passing argument

# required arguments
def sum1(a, b):
    print(a + b)

sum1(2, 9)
 
 
 
# default argument   
def sum2(a, b = 23):
    print(a + b)
    
sum2(2)


# keyword argument
def print_full_name(name1, name2, name3):
    print(name1 + " " + name2 + " " + name3)

# print_full_name(name2="Moid", name1="Abdul", name3="khan")


#variable length argument
# takes argument as tuple
def name(*name):
    print("hello, ", name)
    
# name("Abdul", "Moid", "Khan")


# takes argument as dictionary
def name(**name):
    print(type(name))
    print("hello,", name["fname"], name["lastname"])
    
name(lastname = "Moid khan", fname = "Abdul")

def function(a, b = 2, c = 3):
    return a + b + c

print(function(1, c = 4))

print(function(1, b = 10))