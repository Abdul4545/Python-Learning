# the reduce function is a higher order function that applies a function to a sequence and returns a single value.

# it is a part of the functions module in Python

from functools import reduce

# reduce(function, iretable)

numbers = [1,2,3,4,5]

sum = reduce(lambda x,y: x + y, numbers)
print(sum)

sum = reduce(lambda x,y: x + y, numbers, 12)
print(sum)