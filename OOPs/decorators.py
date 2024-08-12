def greet(fx):
    
    def mfx(*args, **kwargs):
        print("Hello, Good morning")
        fx(*args, **kwargs)
        print("Thanks for using this function")
    
    return mfx
    
@greet
def hello():
    print("hello world")
    
hello()

# greet(hello)()


@greet
def add(a, b):
    print(a + b)

add(3, 7)
    
# greet(add)(2,3)
