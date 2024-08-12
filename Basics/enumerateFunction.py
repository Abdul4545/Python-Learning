a = [12,3,4,5,45]

# index = 0
# for value in a:
#     print(value)
#     if(index == 4):
#         print("Largest value")
        
#     index += 1 



a = [12,3,4,5,45]

index = 0
for index, value in enumerate(a):
    print(value)
    if(index == 4):
        print("Largest value")

print()

# changing the start index 
index = 0
for index, value in enumerate(a, start=1):
    print(value)
    if(index == 4):
        print("Largest value")