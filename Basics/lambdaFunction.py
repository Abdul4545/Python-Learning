# in python a lamabda function us a small function without a name, it is defined using lambda keyword

# def double(x):
#     return x * 2


double = lambda x: x * 2

avg = lambda x,y: (x+y)/2

print(double(5))

print(avg(4,6))

# passing function as parameter
def apply(fx, value):
    return 12 + fx(value)


print(apply(double, 4))

print(apply(lambda x: x * 3, 20))