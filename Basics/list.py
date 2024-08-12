# List is mutable and can store heterogenous data types in it

# Python does not have built-in support for Arrays, but Python Lists can be used instead.

list1 = [1,2,3]
print(list1)

list2 = [1,2,"Moid"]
print(list2)

list3 = [1, 2, 3, True]
print(list3)

list3[3] = 4
print(list3)
print(list3[0])
print(list3[-2])

if 3 in list3:
    print("3 is present in list3")


if "3" not in list3:
    print('"3" is not present in list3')


# List Comprehension
# List comprehensions are used to create new lists from other literals like lists, tuples, dictionaries, sets and even in arrays and strings

list4 = [i for i in range(10)]
print(list)

list5 = [list1, [i for i in list4 if(i%2 ==0)]]

print(list5)


# list methods
list3.append(12)
print(list3)

list6 = [12,10,54,32,56,67]
list6.sort()

print(list6)

list6.sort(reverse= True)
print(list6)

list6.reverse()
list6.index(32)
list6.count(12)


'''

Method	     Description

append()	 Adds an element at the end of the list
clear()	     Removes all the elements from the list
copy()	     Returns a copy of the list
count()	     Returns the number of elements with the specified value
extend()	 Add the elements of a list (or any iterable), to the end of the current list
index()	     Returns the index of the first element with the specified value
insert()	 Adds an element at the specified position
pop()	     Removes the element at the specified position
remove()	 Removes the first item with the specified value
reverse()	 Reverses the order of the list
sort()	     Sorts the list

'''

fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']

fruits.extend(cars)
print(fruits)

newList = cars.copy()
print(newList)

