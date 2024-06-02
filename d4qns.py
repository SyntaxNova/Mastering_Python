num = [1,2,3,4,5,6,7,8,9,0]
list1 = [1,2,3,4,5,6,7,8,9,0]
list2 = [1,4,6,8]
strs = [ "apple" , "banana" , "cherry" , "jackfruit" , "blueberry"]

#  Given a list of numbers, create a function to find the sum
# of all positive numbers"
def SumOfPositiveNum(li):
    if not li:
        return 0
    if li[0] > 0 :
        return li[0] + SumOfPositiveNum(li[1:])
    else:
        return SumOfPositiveNum(li[1:])
# print(SumOfPositiveNum(num ))
    

#  Write a Python function to check if a given string is a
# palindrome"
def palindrome():
    str = input("Enter = ")
    reversed_str = str[::-1]
    if str == reversed_str :
        print("Palindrome ")
    else:
        print("not palindrome ")
    return
# palindrome()


# Implement a function that returns the factorial of a given
# number using recursion"
def factorail (fact):
    if fact == 0 or fact == 1:
        return 1 
    else:
        return factorail(fact-1) * fact
# print(factorail(4))

# Create a function to find the square of each element in a
# given list"
def square(list):
    square_list = []
    for char in list :
        square_list.append(list[char]**2)
        square_list.sort()
    return square_list
# print(square(num))


# Write a function to check if a number is even or odd and
# return "Even" or "Odd" accordingly"
def eve():
    n = int (input("n = "))
    if n % 2== 0:
        print("Even")
    else:
        print("odd")
    return
# eve()


#  Calculate the area of a triangle given its base and height
# using a function"
def area_triangle():
    b = int(input("base = "))
    h = int(input("height = "))
    return 0.5*b*h
# print(area_triangle())


#  Create a function that takes a list of strings and returns
# the list sorted alphabetically"
def sorted_list(list):
    return sorted(list)
# print(sorted_list(strs))

#  Write a function that takes two lists and returns their
# intersection (common elements)"
def intersect(list1 , list2):
    intersection = list(set(list1) and set(list2))
    return intersection
# print(intersect(list1 , list2))

# Implement a function to check if a given year is a leap
# year or not"
def leap_year():
    y = int (input("Enter year = "))
    if (y % 4 == 0 & y % 100 == 0 & y % 400 == 0 ):
        print(f"leap year = {y}")
    else:
        print(f"not leap = {y}") 
# leap_year()


# Create a function that takes a number as input and prints
# its multiplication table.
def table():
    n = int(input("n = "))
    i = 1 
    while i< 11 :
        print(n*i , end =" ")
        i+=1
    return
# table()