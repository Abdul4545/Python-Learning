# The map() is higher order function that executes a specified function for each item in an iterable (list, tuple, str, dict, set, range, etc.). The item is sent to the function as a parameter and returns a new squence containing the transformed elements


# Syntax
# map(function, iterables)

def myfunc(n):
  return n*n

# list1 = [1,2,3,4,5]
tuple1 = (1,2,3,4,5)

x = map(myfunc, tuple1)
# returns a map object then we can convert into list tuple

# x = list(map(myfunc, list1))
# x = tuple(map(myfunc, tuple1))

print(x)


def myfunc(a, b):
  return a +" " + b

x = tuple(map(myfunc, ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple')))

print(x)

tuple2 = tuple(map(lambda x: x * 2, tuple1))
print(tuple2)
