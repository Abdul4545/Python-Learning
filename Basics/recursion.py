def printing(n):
    if n > 5:
        return

    printing(n+1)
    print(n)
            
# printing(1)


def factorial(n):
    if(n < 0):
        return "factorial not possible"
    
    if(n == 0 or n == 1):
        return 1
    
    else:
        return n * factorial(n-1)
    

# print(factorial(-10))
# print(factorial(0))
# print(factorial(5))

