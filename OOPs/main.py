# The first is used to initialise newly created object, and receives arguments used to do that:

class Foo:
    def __init__(self, a, b, c):
        print(a+b+c)


x = Foo(1, 2, 3) 
# __init__


# The second implements function call operator.
class Foo:
    def __call__(self, a, b, c):
        print(a+b+c)

x = Foo()
x(1, 2, 3) # __call__