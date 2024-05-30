# DAY 01 of Mastring Python 
# Solving 10 problems

# ") Write a Python program to calculate the area of a
# rectangle given its length and width+
#               program
l = int(input("enter length = "))
b = int(input("enter breadth = "))
print("area og rectangle = " , l*b)


# ) Create a program that takes a user's name and age as
# input and prints a greeting message+
#               program
name = input('enter name = ')
age = int(input("enter age = "))
print("greetings " , name ,"!")


# %) Write a program to check if a number is even or odd+
#               program
a=int(input("enter a = "))
if(a%2 == 0):
    print("even")
else:
    print("odd")


# ) Given a list of numbers, find the maximum and minimum
# values+
#               program
numbers = [1,2,3,4,5,6,7,8,9,0]
numbers.sort()
print("minimum = " , numbers[0])
print("maximum = " , numbers[len(numbers)-1])


# ) Create a Python function to check if a given string is a
# palindrome+
#               program
str = "racecar"
if(str == str[::-1]): # reverse string
    print("palindrom")
else:
    print("Not a palindrom")



# ) Calculate the compound interest for a given principal
# amount, interest rate, and time period+
#               program
principle = float(input("Enter principle amount "))
rate = float(input("Enter rate "))
time = float(input("enter time period "))
n = float(input("enter number of times interst is applied per time period "))
compound_interset = principle*(1+rate/n)**(n*time) #compunt interest formula
print(compound_interset-principle)

# ) Write a program that converts a given number of days
# into years, weeks, and days+
#               program
days = int (input("days = "))
years = days // 365
remaining_days = days % 365
weeks = remaining_days // 7
day = remaining_days % 7
print("output = " , years ,"years " , weeks , "weeks " , day , "days")


# ) Create a program that takes a sentence as input and
# counts the number of words in it+
#               program
str1 = "hi i am atharva"
words = str1.split()
print(len(words))

# " ) Implement a program that swaps the values of two
# variables.
a= 2
b= 3
print(a,b)
c= 0
c=a
a=b
b=c
print(a,b)