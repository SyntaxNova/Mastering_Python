def avg(a,b,c) :
    return (a+b+c)/3
# print(avg(2,2,2))




def length (list):
    return len(list)
list = [1,2,3,4,5,6,7,8,9,0]
# print(length(list))




def printel(list):
    for char in list:
        print(char , end = " ")
# printel(list)


def factorial():
    n = int(input("n = "))
    fact = 1
    i = 1
    while i < n+1 :
        fact *= i
        i += 1
    return fact

# print(factorial(n))


def convert():
    usd = int(input("usd = "))
    return 84 * usd
# print(convert(n))   

def eve():
    n = int(input("n = "))
    if n%2 == 0 :
        print("Even")
    else:
        print("odd")       
# eve()

def sumn(n):
    if (n == 0 ):
        return 0
    return sumn(n-1) + n
# print(sumn(2))


def printlist(list , i =0):
    if i == len(list):
        return 0
    print(list[i] , end=" ") 
    printlist(list,i+1)
    
# printlist(list)