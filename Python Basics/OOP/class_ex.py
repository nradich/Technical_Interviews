class Employee:
    #creating a function within my class, designating the init component
    #using the self.attribute to define a new employee attributes within the class
    #after self as first parameter, would then add in the other attributes that we want the class to contain explicitly

    #best practice is name the variables the same as the paramters within the defining class ie Name = Name
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary

    def increase_salary(self, percent):
        """Function within employee class, not in the global"""
        #the += allows us to add the product of the right hand side of the equal sign to the left 
        #don't access the same as dictionaries
        self.salary += self.salary * (percent/100)

    #going from employee to self as the lone parameter
    def employee_info(self):
        """Method"""
        print(f"{self.name} is {self.age} years old. Employee is a {self.position} with the salary of ${self.salary}")

#e1 = Employee()
e2 = Employee('Jonathan', 20, 'typer', 125)
e3 = Employee('yogi', 25, 'dawg', 50)
e3.increase_salary( 25)
e3.employee_info()