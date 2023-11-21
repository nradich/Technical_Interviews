class Employee:
    #creating a function within my class, designating the init component
    #using the self.attribute to define a new employee attributes within the class
    #after self as first parameter, would then add in the other attributes that we want the class to contain explicitly

    #best practice is name the variables the same as the paramters within the defining class ie Name = Name
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.set_salary(salary)

    def increase_salary(self, percent):
        """Function within employee class, not in the global"""
        #the += allows us to add the product of the right hand side of the equal sign to the left 
        #don't access the same as dictionaries
        self.salary += self.salary * (percent/100)

    #going from employee to self as the lone parameter
    def __str__(self):
        """Method"""
        return(f"{self.name} is {self.age} years old. Employee is a {self.position} with the salary of ${self.salary}")
    
    def __repr__(self) -> str:
        return (
        f"Employee({repr(self.name)} , {repr(self.age)},"
        f"{repr(self.position)},  {repr(self.salary)})")
    
    @property
    def get_salary(self):
        """Return salary, can put in parameters to limit end user interface"""
        return print(self.salary)
    
    def set_salary(self, salary:int):
        """Allows input of new salary, must be above minimum salary of 1000"""
        if salary < 1000:
            raise ValueError("Minimum salary is $1000")
        self.salary = salary

    @property
    def annual_salary(self):
        """Computed propery"""
        #that would add it to the class
        ## self.annual_salary = salary * 12
        #or could calculate it
        return self.salary * 12  
    

#Working on Inheritance
class NewEmployee:
    organization = "Business_Unit"
    minimum_wage = 1000


    @classmethod
    def change_minimum_wage(cls, new_wage):
        """Class method restricting the min wage """
        if new_wage > 3000:
            raise ValueError("Company has no money")
        cls.minimum_wage = new_wage

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    
    def increase_salary(self, percent):
        """Function within employee class, not in the global"""
        #the += allows us to add the product of the right hand side of the equal sign to the left 
        #don't access the same as dictionaries
        self.salary += self.salary * (percent/100)

class Tester(NewEmployee):
    organization = "tester"
    def run_test(self):
        print(f"Testing is started by {self.name}")
        print("Tests are done.")

    def increase_salary(self, percent):
        """Function within employee class, not in the global"""
        #the += allows us to add the product of the right hand side of the equal sign to the left 
        #don't access the same as dictionaries
        self.salary += self.salary * ((percent+5)/100)

class Developer(NewEmployee):
    def increase_salary(self, percent):
        """Function within employee class, not in the global"""
        #the += allows us to add the product of the right hand side of the equal sign to the left 
        #don't access the same as dictionaries
        self.salary += self.salary * (percent/100)

#setting the new epmployee as a tester, ie their role
homer = Tester("Homer", 25, 2000)
hazel = Developer("Hazel", 30, 2000)
homer.increase_salary(20)
print(homer.salary)
homer.increase_salary(20)
hazel.increase_salary(20)
print(f"Homer's salary is {homer.salary}")
print(f"Hazel's salary is {hazel.salary}")

print(f"Homer's organization is {homer.organization}")
print(f"Hazel's organization is {hazel.organization}")

hazel.change_minimum_wage(500000)

#e1 = Employee()
e2 = Employee('Jonathan', 20, 'typer', 1100)
e3 = Employee('yogi', 25, 'dawg', 5000)
# e3.increase_salary( 25)
# print(e3)
# print(repr(e3))

#tried to set salary below min, got error
e2.set_salary(2000)
#after making it a propery, don't need to use paranthesis to call the method 
e2.get_salary
print(e2.annual_salary)