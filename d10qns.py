#  Create a base class Shape with methods to calculate area
# and perimeter, and derive classes Circle and Square
import math
class Shape:
    def __init__(self):
        pass
        
    def area(self):
        pass
           
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self , radius):
        super().__init__()
        self.radius = radius
        
    def area(self):
        return math.pi* self.radius**2
    
    def perimeter(self):
        return 2*math.pi*self.radius

class Square(Shape):
    def __init__(self , side):
        super().__init__()
        self.side = side
        
    def area(self):
        return self.side**2
    
    def perimeter(self):
        return 4*self.side  
    
Circle1 = Circle(3)
Square1 = Square(4)
# print(f"Area of circle = {Circle1.area()} , Perimeter of circle = {Circle1.perimeter()}\nArea of square = {Square1.area()} , perimeter of Square = {Square1.perimeter()}")    



#  Implement a class hierarchy to represent different types
# of employees (Manager, Engineer) with their attributes
class Employees:
    def __init__(self, name  , salary) -> None:
        self.name = name
        self.salary = salary
    
    def getDetails(self):
        pass

class Manager(Employees):
    def __init__(self, name, salary , role):
        super().__init__(name, salary)
        self.role = role
        
    def getDetails(self):
        print(f"Manager Name = {self.name}  \nSalary = {self.salary}  \ndepartment = {self.role}")
        
class Engineer(Employees):
    def __init__(self, name, salary , departmet) -> None:
        super().__init__(name, salary)
        self.departmet = departmet
        
    def getDetails(self):
        print(f"Enginner Name = {self.name}  \nSalary = {self.salary}  \ndepartment = {self.departmet}")

m1 = Manager("Atharva" , "30,00,000" , "Finance")
e1 = Engineer("arjun" , "10,000" , "IT")
# m1.getDetails()
# print("")
# e1.getDetails()



#  Write a Python program that uses inheritance to
# represent a hierarchy of shapes (Triangle, Rectangle,
# etc.
# it is same as qns 1i have just changed the names but formulas are same need to chnage
import math
class Shapes:
    def __init__(self , name):
        self.name = name
        
    def area(self):
        pass
           
    def perimeter(self):
        pass

class Triangle(Shapes):
    def __init__(self , radius):
        super().__init__("Triangle")
        self.radius = radius
        
    def area(self):
        return math.pi* self.radius**2
    
    def perimeter(self):
        return 2*math.pi*self.radius

class Rectangle(Shapes):
    def __init__(self , side):
        super().__init__("Rectangle")
        self.side = side
        
    def area(self):
        return self.side**2
    
    def perimeter(self):
        return 4*self.side  
    
Triangle1 = Triangle(3)
Rectangle1 = Rectangle(4)
# print(f"Area of circle = {Triangle1.area()} , Perimeter of circle = {Triangle1.perimeter()}\nArea of square = {Rectangle1.area()} , perimeter of Square = {Rectangle1.perimeter()}")    



#  Create a class hierarchy to represent different types of
# animals (Bird, Fish) with their own attributes and
# methods
class Animals:
    def __init__(self , type):
        self.type = type
    def make_voice(self):
        pass
    def move(self):
        pass

class Bird(Animals):
    def __init__(self, breed , region):
        super().__init__("Bird")
        self.breed = breed
        self.region = region
        
    def make_voice(self):
        print(f"Bird of {self.breed} is chirping...")
        
    def move(self):
        print(f"{self.breed} has moved to region {self.region}")
        
class Fish(Animals):
    def __init__(self , speed):
        super().__init__("Fish")
        self.speed = speed
        
    def make_voice(self):
        print(f"{self.type} is making voice as Bluh..Bluh")
        
    def move(self):
        print(f"{self.type} has moveed with spped of {self.speed}")
        
b1 = Bird("piegon" , "Asia")
f1 = Fish("10 kmph")
# b1.make_voice()
# b1.move()
# f1.move()
# f1.make_voice()



# Given a JSON file with product details (name, price,
# quantity), create a Product class with encapsulated
# attributes0



#  Implement a program that uses inheritance to represent a
# hierarchy of vehicles (Car, Bike, Truck, etc.)
class Vehicle:
    def __init__(self , type):
        self.type = type
    
    def start(self):
        return f"{self.type} is Started..."
    
    def stop(self):
        return f"{self.type} is stoped."

    def funct(self):
        print( f"{self.stop()} , {self.start()}")
    
class Bike(Vehicle):
    def __init__(self , Bike_Model):
        super().__init__("Bike")
        self.Bike_Model = Bike_Model
        
class Truck(Vehicle):
    def __init__(self , Truck_Model):
        super().__init__("Truck")
        self.Truck_Model = Truck_Model
        
class Car(Vehicle):
    def __init__(self , Car_Model):
        super().__init__("Car")
        self.Car_Model = Car_Model
c1 =  Car("i10")
t1 = Truck("Tata")
b1 = Bike("Supra")
# c1.funct()
# t1.funct()
# b1.funct()



#  Write a Python program that uses encapsulation to
# protect sensitive information in a User class.
class user:
    def __init__(self , userid , password):
        self.__userid = userid
        self.__password = password
    
    def set_userid(self , uid):
        return self.__userid == uid
        
    def set_pass(self , passw):
        return self.__password == passw
        
    def get_uid(self):
        return self.__userid
       
    
    
#  Given a CSV file with employee details (name, position,
# salary), create an Employee class with private attributes(
class Employee:
    def __init__(self , name , position , salary):
         self.__name = name
         self.__position = position 
         self.__salary = (salary)
         
    def __str__(self):
        return f"name = {self.__name} , pos = {self.__position} , salary = {self.__salary}"

import csv
def readFile(csvfile):
    employees = []
    with open(csvfile , "r") as file :
        data = csv.reader(file)
        next(data)
        for row in data:
            name,position,salary = row
            emp = Employee(name,position,salary)
            employees.append(emp)
    return employees

e1 = readFile("files/employees.csv")
for employee in e1:
    print(employee)