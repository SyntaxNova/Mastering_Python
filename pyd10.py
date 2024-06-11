class Circle:
    def __init__(self , r):
        self.r = r
        
    def area(self):
        print(self.r*2*3.14)
        
    def perimeter(self):
        print(3.14*self.r*self.r)
c1 = Circle(3)
# c1.area()
# c1.perimeter()

class Employee:
    def __init__(self , role , department , salary) :
        self.role = role
        self.department = department
        self.salary = salary
        
    def ShowDetails(self):
        print(f"role = {self.role}\ndepartment = {self.department} \nsalary = {self.salary}")
        
class Engineer(Employee):
    def __init__(self, name , age):
        super().__init__("role", "department", "salary")
        self.name = name
        self.age = age
        
class Order:
    def __init__(self , item , price):
        self.item = item
        self.price = price
        
    def __gt__(self , ordr2):
        return self.price > ordr2.price
        
Order1 = Order(1,300)
Order2 = Order(2,250)
print(Order1 > Order2)
        
        
        
employeeOne = Employee("swe2" , "Project Management" , 3000000)
# employeeOne.ShowDetails()
engg1 = Engineer("Atharva" , 20)



    