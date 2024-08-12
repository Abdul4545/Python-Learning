
# "r" - Read - Default value. Opens a file for reading, error if the file does not exist

# "a" - Append - Opens a file for appending, creates the file if it does not exist

# "w" - Write - Opens a file for writing, creates the file if it does not exist

# "x" - Create - Creates the specified file, returns an error if the file exists

# "t" - Text - Default value. Text mode

# "b" - Binary - Binary mode (e.g. images)


# f = open("D:\\myfiles\welcome.txt", "r")

# open a file in read mode
# f = open(".//Basics/demofile.txt")
# f = open(".//Basics/demofile.txt", "r")

# print(f.read()) 
# reads whole file content

# print(f.read(10)) 
# reads only 10 characters

# print(f.readline())
# reads only 1st line of file and keeps the pointer on next line
# print(f.readline())

# looping through the file
# for x in f:
#   print(x)

# print(f.readlines())
# reads whole file content and stores in list including "\n"

# f.close()



# append mode 
# f = open(".//Basics/demofile.txt", "a")
# f.write("\nNow the file has more content!")
# f.close()

# f = open(".//Basics/demofile.txt", "r")
# print(f.read())
# f.close()


# write mode
# f = open(".//Basics/demofile.txt", "w")
# f.write("Woops! I have deleted the content!")
# f.close()

# f = open(".//Basics/demofile.txt", "r")
# print(f.read())


# Create a New File
# To create a new file in Python, use the open() method, with one of the following parameters:

# "x" - Create - will create a file, returns an error if the file exist

# "a" - Append - will create a file if the specified file does not exist

# "w" - Write - will create a file if the specified file does not exist


# Delete a File

# import os
# os.remove("demofile.txt")

# Check if file exists, then delete it
# import os
# if os.path.exists("demofile.txt"):
#   os.remove("demofile.txt")
# else:
#   print("The file does not exist")


# with open("myfile.txt", "a") as f:
#     f.write("Hey i am inside with")


# seek() method
with open("myfile.txt", "r") as f:
    # moves to the 10th byte in the file
    f.seek(10)
    
    print(f.tell())
    data = f.read(5)    
print(data)




# The truncate() method resizes the file to the given number of bytes.

# If the size is not specified, the current position will be used.

