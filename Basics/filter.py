# The filter() function is a higher order function that returns an iterator where the items are filtered through a function to test if the item is accepted or not.

# filter(function, iterable)


list1 = [1,2,3,4,5]

def function(x):
    if x % 2 == 0:
        return x
    

square = list(filter(function, list1))
print(square)




# Filter the array, and return a new array with only the values equal to or above 18
ages = [5, 12, 17, 18, 24, 32]

def myFunc(x):
  if x < 18:
    return False
  else:
    return True

adults = filter(myFunc, ages)

for x in adults:
  print(x)
