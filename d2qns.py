# (, Given a list of numbers, find the sum and average
# n = [1,2,3]
# average = sum(n) / len(n)
# print("Sum = ", sum(n))
# print("average = {average}")




# , Create a program that takes a temperature in Celsius and
# converts it to Kelvin
# temp = float(input("temperature in celcius = "))
# print("temp in kelvin = ",(temp + 273.0))




# ), Implement a program that checks if a given string is a
# palindrome

# str = str(input("Enter str = "))

# reversed_str = str[::-1]

# if(str == reversed_str):
#     print(" palindrome")
# else:
#     print("Not palindrome")





# , Create a function to reverse a given string
# def reverse (str) :
#     new_str = str[::-1]
#     return new_str

# a = "atharva"
# print(reverse(a))





# #, Given a list of names, concatenate them into a single
# string separated by spaces
# names = ["name1" , "name2" , "name3"]

# single_str = " ".join(names)
# print(single_str)



# , Write a Python program to check if a given string is a
# pangram (contains all letters of the alphabet)
# import string
# s = "The quick brown fox jumps over a lazy dog"
# alpha = set(string.ascii_lowercase)
# s = s.lower()
# new_set = set(s)
# print(alpha.issubset(new_set))



# , Calculate the area and circumference of a circle given its
# radius
# r = 3
# area = 3.14 * ( r ** 2)
# c = 2 * 3.14 * r
# print("area = " , area)
# print("circumference = " , c)





# , Implement a program that converts a given number of
# minutes into hours and minutes

# minutes = int(input("minutes =  "))

# hrs = minutes // 60
# r_min = minutes % 60

# print('hrs = ' , hrs ,'Mins = ' , r_min )





# , Create a function to count the number of vowels in a
# given string

# def vowels (str):
#     v = set('aeiouAEIOU')
#     str = str.lower()
#     new_str = set(str)
    
#     count = 0
#     for char in str :
#         if char in v:
#             count += 1
#     return count
    
# s = "aeiou aeiou"
# print(vowels(s))





# ( , Write a program to check if a number is prime.
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

number = 7 
print(f"Is {number} prime? \n{is_prime(number)}")