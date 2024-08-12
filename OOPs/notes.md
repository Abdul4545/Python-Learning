Class
Objects
Encapsulation
Inheritance
Polymorphism
Abstraction

**What is Class ?**
a class is a blueprint for creating objects (instances). A class defines a set of attributes and methods that the objects created from the class will have.


**Object**: An instance of a class. Objects have attributes and behavior as defined by the class.

**Attribute**: A variable that belongs to a class or an instance of a class.

**Method**: A function that is defined inside a class and operates on instances of that class.


**Advantage/Application of constructors**
Background check in companies
Internet check for apps
like ola youtube do not open if net is not connected

**self**
-> self is the reference to the object created of our class

-> it is automatically passed whenever we are calling any method, and in the method definition also it is needed to be passed.

-> only an object can access or can be helpful in connecting attributes and methods inside our class


**Instance Variable**
cn = ComplexNumber(3,3)
cn1 = ComplexNumber(5,-5)

cn and cn1 are instance variables which have different values of attribute 


**Access Modifiers**

**public** 
by default access modifier is public


**private**
we make attributes private by using __ before it
example: self.__mark


**protected**
can be accessed in the class and its subclasses
use use _ before it
example: def _logout():
            pass

**Static property / Variables**
They are defined outside of the methods at class level
owned by class majorly but accessible by objects
We can have static method as well decorated with
**@staticmethod**


**Encapsulation**
The binding of our data members/attributes and methods in a single unit is called as encapsulation
Example: In student class we have used encapsulation


**Inheritance**
we inherit
--> non private attributes
--> non private methods
--> constructor
--> other magic methods



we can not inherit
--> We can not access private attributes or methods of parent class
--> parent class can not inherit from child class

**super keyword**
super() is used to access methods of parent class from child class

can not be used outside
can only access method not attributes


**Single Inheritance**
**Description:** A class inherits from only one parent class.


**Hierarchical Inheritance**
**Description**: Multiple classes inherit from the same parent class.

Buyer Inherits User for amazon
Seller inherits user for amazon


**Multilevel Inheritance**
**Description**: A class inherits from a parent class, which in turn inherits from another parent class.

--> lower levels get properties from above levels
--> super() of each class can reach out to just the parent

**Multiple Inheritance**

Ambiguity is resolved in the order of inheritance 
MRO (method resolution order)


**Polymorphism**
In python we achieve polymorphism by
1) Method Overriding
2) Method Overloading
3) Operator Overloading



**Abstraction**

Fundamental concept of OOPs that involves hiding complex implementation details and showing essential features

Example: Phone, tv remote volume up down changing channel

take call , make call -> In this we dont know the internal working of how call comes to our mobile and goes from our mobile

**from abc import ABC, abstractmethod**
we have to ensure 2 things
1) Inherit abc class
2) Should have atleast 1 abstract method
