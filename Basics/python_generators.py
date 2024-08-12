# Generators in python are special type of functions that allow us to create an iterable sequence of values.
# Generator function returns a generator object, which can be used to generate the values one by one as you iterate over it.

def my_generator():
    for i in range(5):
        yield i

# The yield statement returns a value from the generator and suspends the execution of the function until the next value is requested
        
gen = my_generator()
# print(gen)

for j in gen:
    print(j)
    
# print(next(gen))