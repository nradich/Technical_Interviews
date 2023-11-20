### Fundamentals

why we need OOP, dictionaries allow for more precise navigation of nested objects, as opposed to trying to slice lists 

### Designing a Class

**Class** blueprint for creating an object, or object factory, holds the associated attributes, 
classes can hold functions are well 

dot notation can access functions and elements within the class

Review '__init__' and (self) components
allows for new instantialition of objects, I believe

When calling a class, we are instantioning an object

We don't access attributes within a class the same as a dictionary ie with brackets.
We use the dot notation

Methods are functions within the class

Can implicitily call instances of the class instead of the class itself

by using the self variable, can simply call the method of the class 
`Employee.increase_salary(employee1, 25%)` to `employee1.increase_salary(25)`

To have a a class description print out, define a method called the "__str__" parameter 
`def __str__(self):
    return 'string about this class`

the eval function, globally available, allows for python to intepret a string as code
ie eval("2+2"), we would want the repr function from our class to be able to be easily inserted into this
The repr function should allow you to create a new instance of the class from the eval function
ie eval(repr(new_variable))