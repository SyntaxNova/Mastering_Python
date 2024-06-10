#  Create a class to represent a Student with attributes like
# name, age, and grades
class student:
    def __init__(self , name , age , grades):
        self.name = name
        self.age = age
        self.grades = grades
    
s1 = student("atharva" , 20 , 9.45)
# print(s1.name , s1.age , s1.grades)



#  Given a CSV file with employee details (name, position,
# salary), create a class to represent an Employee
class emp:
    def __init__(self , name , pos , salary):
        self.name = name
        self.pos = pos
        self.salary = salary
    def __str__(self):
        return f"Name: {self.name}, Position: {self.pos}, Salary: {self.salary}"
        
def emps(csvfile):
        import csv
        employees = []
        with open(csvfile , "r") as file:
            data = csv.DictReader(file)
            for row in data: 
                empl = emp(row['name'] , row['position'] , row['salary'])
                employees.append(empl)
        return employees
    
# csvfile = "files/employees.csv"
# e1 = emps(csvfile)
# for e in e1:
#     print(e)



#  Implement a program that simulates a basic bank account
# using a BankAccount class
class BankAccount:
    def __init__(self , bal , acn):
        self.bal = bal
        self.acn = acn
    
    def debited(self , amt):
        self.bal -= amt
        print(f"debited {amt} avlable balance {self.bal}")
        
    def credited(self , amt):
        self.bal += amt
        print(f"credited {amt} avlable balance {self.bal}")
a1 = BankAccount(1000 , 1)
# print("balance = " , a1.bal)
# a1.debited(500)
# a1.credited(600)



#  Write a Python program that uses a Rectangle class to
# calculate the area and perimeter of a rectangle
class rectangle:
    def __init__(self , l , b):
        self.l = l
        self.b = b
        
    def area(self):
        return self.l*self.b

    def perimeter(self):
        return 2*(self.l+self.b)
r1 = rectangle(1,1)
# print("length = ", r1.l)
# print("breadth = ", r1.b)
# print("are of rect = " , r1.area())
# print("perimeter of rect = " , r1.perimeter())



#  Create a class to represent a Car with attributes like
# make, model, and year
class car:
    def __init__(self , make , model , year):
        self.make = make
        self.model = model
        self.year = year
    
    def printinfo(self):
        print(self.make , "\n" , self.model , "\n" , self.year)
car1 = car("hyndai" , "i10 sports" , 2012)
# car1.printinfo()



#  Write a program that uses a Person class to keep track of
# a person's name, age, and address
class person:
    def __init__(self,name, age, address):
        self.name = name
        self.age = age
        self.address = address
    def __str__(self) :
        return f"Name: {self.name} Age: {self.age} address: {self.address}"
p1 = person("a" ,20 , "india")
# print(p1)



#  Implement a program that uses a Circle class to calculate
# the area and circumference of multiple circles
class circle:
    def __init__(self , radius):
        self.radius = radius
    def area(self):
        print(self.radius*self.radius*3.14)
    def circumference(self):
        print(2*self.radius*3.14)
c1 = circle(3)
# print("r = " , c1.radius)
# c1.area()
# c1.circumference()



#  Given a CSV file with product details (name, price,
# quantity), create a Product class to manage the data
class product:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = float(price)
        self.quantity = int(quantity)
        
    def __str__(self):
        return f"Name :{self.name}, price : {self.price}, quantity : {self.quantity}"

import csv
def read_csvfile(csf):
    products = []
    with open(csf , "r") as f:
        reader = csv.DictReader(f) 
        for row in reader:
            productn = product(row["name"],row["price"],row["quantity"])
            products.append(productn)
    return products
    
csf = "files/product.csv"
produc = read_csvfile(csf)
for pro in produc:
    print(pro)



# Create a class to represent a Movie with attributes like
# title, director, and rating.
class Movie:
    def __init__(self, title, director, rating):
        self.title = title
        self.director = director
        self.rating = float(rating)
        
    def set_title(self,title):
        self.title = title
        
    def get_title(self):
        return self.title 
    
    def set_director(self , director):
        self.director = director
        
    def get_director(self):
        return self.director 
    
    def set_rating(self , rating):
        self.rating = rating
        
    def get_rating(self):
        return self.rating
    
    def __str__(self) -> str:
        return f"title : {self.title} , director: {self.director} , rating: {self.rating}" 
    
movie1 = Movie("Inception", "Christopher Nolan", 8.8)
movie2 = Movie("The Matrix", "Lana Wachowski, Lilly Wachowski", 8.7)

print("Movie 1 Title:", movie1.get_title())
print("Movie 1 Director:", movie1.get_director())
print("Movie 1 Rating:", movie1.get_rating())

movie1.set_title("Inception: The Beginning")
movie1.set_rating(9.0)

print("Updated Movie 1 Info:")
print(movie1)

print("Movie 2 Info:")
print(movie2)
