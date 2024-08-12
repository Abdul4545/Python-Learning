x = int(input("Enter the value of x : "))

# break is not needed in this
#only first match is printed
match x:
    case 0:
        print("it is zero")
        
    case 4:
        print("It is 4")
        
        
    case _ if x != 90:
        print(x, " is not equal to 90")
        
    case _ if x != 23:
        print(x, " is not equal to 23")
        
    case _ :
        print("default case")