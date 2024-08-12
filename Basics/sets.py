# A set is a collection which is unordered, unchangeable*, and unindexed.

# * Note: Set items are unchangeable, but you can remove items and add new items

# Set items are unordered, unchangeable, and do not allow duplicate values.

# Note: The values True and 1 are considered the same value in sets, and are treated as duplicates, False and 0 are considered the same value in sets

myset = {"apple", "banana", "cherry"}
print(myset)

thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)
print(len(thisset))

set1 = {"abc", 34, True, 40, "male"}


# Using the set() constructor to make a set:

thisset = set(("apple", "banana", "cherry")) 
# note the double round-brackets
print(thisset)


# Access Items

# We cannot access items in a set by referring to an index or a key.

# But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.

for x in thisset:
    print(x)
    
print("banana" in thisset)


# Add Items

thisset.add("orange")
print(thisset)

# adding 2 sets
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)
print(thisset)

#adding any iterable
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)



# Methods

'''

Method	                        Shortcut	        Description
add()	 	                                        Adds an element to the set
clear()	 	                                        Removes all the elements from the set
copy()	 	                                        Returns a copy of the set
difference()	                    -	            Returns a set containing the difference between two or more sets
difference_update()	                -=	            Removes the items in this set that are also included in another, specified set
discard()	 	                                    Remove the specified item
intersection()	                    &	            Returns a set, that is the intersection of two other sets
intersection_update()	            &=	            Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	 	                                Returns whether two sets have a intersection or not
issubset()	                        <=	            Returns whether another set contains this set or not
 	                                <	            Returns whether all items in this set is present in other, specified set(s)
issuperset()	                    >=	            Returns whether this set contains another set or not
 	                                >	            Returns whether all items in other, specified set(s) is present in this set
pop()	 	                                        Removes an element from the set
remove()	 	                                    Removes the specified element gives error if not present
symmetric_difference()	            ^	            Returns a set with the symmetric differences of two sets (not common in both sets)
symmetric_difference_update()	    ^=	            Inserts the symmetric differences from this set and another
union()	                            |	            Return a set containing the union of sets
update()	                        |=	            Update the set with the union of this set and others

'''