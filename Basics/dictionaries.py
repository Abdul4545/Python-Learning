# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

#### As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(thisdict)
print(thisdict["brand"])

# Dictionaries cannot have two items with the same key
# Duplicate values will overwrite existing values

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020,
  1: 12
}
print(thisdict)
print(len(thisdict))

# The values in dictionary items can be of any data type

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

print(thisdict)


# Using the dict() method to make a dictionary

thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)


# Accessing Items
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]

# There is also a method called get() that will give you the same result
x = thisdict.get("model")

x = thisdict.keys()

print(x)

# Add a new item to the original dictionary
thisdict["color"] = "white"

x = thisdict.values()
print(x)

x = thisdict.items()
print(x)

if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")
  
  
# Change Values
thisdict["year"] = 2018
print(thisdict)

thisdict.update({"year": 2020})
# If the item does not exist, the item will be added.
print(thisdict)

thisdict.pop("model")


# the popitem() method removes the last inserted item

# thisdict.popitem()
# print(thisdict)

# del thisdict["model"]
# print(thisdict)

del thisdict
# print(thisdict) 
#this will cause an error because "thisdict" no longer exists.


# thisdict.clear()
# The clear() method empties the dictionary
# print(thisdict)



thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# Print all key names in the dictionary, one by one
for x in thisdict:
  print(x)

print()  

# Print all values in the dictionary, one by one
for x in thisdict:
  print(thisdict[x])
  
  
for x in thisdict.values():
  print(x)
  


for x in thisdict.keys():
  print(x)
  
  
for x, y in thisdict.items():
  print(x, y)
  
  
mydict = thisdict.copy()
print(mydict)


mydict = dict(thisdict)
print(mydict)



# Nested Dictionaries

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}



child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(myfamily["child2"]["name"])

for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])
