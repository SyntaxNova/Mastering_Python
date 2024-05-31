i = 0
while i < 100 :
    print(i+1)
    i+=1

i = 100
while i > 0 :
    print(i)
    i-=1

i = 1
n = int(input("enter table = "))
while i <= 10 : 
    print(i*n)
    i+=1
i=1
while i <= 10 :
    print(i**2) 
    i+=1
    
tup = (1,
4,
9,
16,
25,
36,
49,
64,
81,
100)

x = int(input("Enter x = "))
i = 0
while i < 10 :
    if (tup[i] == x): 
        print("found x at position i = " , i)
    i += 1 
    
for num in tup :
    print(num)
    
for char in tup :
    print (char)
    if (char == x ):
        print ("found ")


i = 0 
n=int(input("n = "))
sum = 0
while i <= n :
    sum += i
    i += 1
print(sum)

fact = 1
for num in range( 1 , n+1 ):
    fact *=  num
print("factorial = " , fact)

