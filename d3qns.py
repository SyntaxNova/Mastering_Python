# 0 Create a program that takes a year as input and checks if
# it is a leap year or not)


# 0 Given a list of integers, find all the even numbers and
# store them in a new list)
integers = [1,2,3,4,5,6,7,8,9]
even = []
i = 0 
while i < len(integers):
    if integers[i] % 2 == 0 : 
        even.append(integers[i])
    i += 1
print (even)





# -0 Write a Python program to check if a given number is a
# prime number)
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
print(f"Is {number} prime? {is_prime(number)}")





# 0 Create a program that generates the Fibonacci sequence
# up to a given number of terms)
n = int(input("Enter number of terms = "))
fibo = [0,1]
i = 0 
while i < n :
    sum = fibo[i] + fibo[i+1]
    fibo.append(sum)
    i+=1
print (fibo)



# 0 Given a list of names, print all names starting with the
# letter 'A')
names = ["Atharva" , "Arjun" , "narayan" , "vishnu" , "Ashoka"]
new_namesA = []
i = 0
while i < 5:
    if  names[i][0] == 'A' :
        new_namesA.append(names[i])
    i+=1
print(new_namesA)   
    
    
    
    
    

# 0 Implement a program that prints the multiplication table
# of a given number)
n = int(input("Enter n = "))
i = 0
while i < 10:
    print(n*(i+1))
    i+=1





# 0 Write a program that calculates the factorial of a given
# number)
i = 1 
fact = 1
n = int(input("Fact no = "))
while i <= n :
    fact *= i
    i+=1
    
print ("Factorial = " ,fact)

    

# 0 Create a loop that prints all prime numbers between 1 and
# 50)



# 0 Given a list of words, count the number of words with
# more than five characters)
words = ["Atharva" , "Arjun" , "narayan" , "vishnu" , "Ashoka" , "ABC"]
count = 0 
for word in words :
    if len(word) >= 5 :
        count+=1
print(count)

    
    


#  0 Calculate the sum of digits of a given number.
num = str (input("ENter digit = "))
sum = 0 
s = set(num)
for char in num:
    d = int(char)
    sum += d
print(sum)

    



