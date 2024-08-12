"""

The try block lets you test a block of code for errors.

The except block lets you handle the error.

multiple except block can be there

The else block lets you execute code when there is no error.

The finally block lets you execute code, regardless of the result of the try- and except blocks.

"""

# try:
#   print(x)
# except:
#   print("An exception occurred , x is not defined")
  

"""

Since the try block raises an error, the except block will be executed.

Without the try block, the program will crash and raise an error

print(x)
"""


# try:
#   print(x)
# except NameError:
#   print("Variable x is not defined")
# except:
#   print("Something else went wrong")
  
  

# try:
#   print("Hello")
# except:
#   print("Something went wrong")
# else:
#   print("Nothing went wrong")
  



# try:
#   print(x)
# except:
#   print("Something went wrong")
# finally:
#   print("The 'try except' is finished")
  
  


# try:
#   f = open("E:\\Python\\Basics\\demofile.txt", "w+")
#   try:
#     f.writelines("Lorum Ipsum")
#     print("successfully written into file")
#   except Exception as e:
#       print(e)
#   finally:
#     f.close()
# except:
#   print("Something went wrong when opening the file")



# Raise an exception / Custom error

x = -1
if x < 0:
  raise ValueError("Sorry, no numbers below zero")



# x = "hello"
# if not type(x) is int:
#   raise TypeError("Only integers are allowed")


print((type(int)))