#  Write a Python program to copy the contents of one text
# file into another2
with open("f1.txt" , "r") as f:
    data = f.read()
with open("f2.txt" , "w") as f:
    f.write(data)



#  Given a CSV file with student names and scores, find the
#  student with the highest score
import csv
with open("s.csv" , "r") as f:
    d = csv.reader(f)
    next(d)
    top_stud = ''
    maxsc = -1
    
    for row in d:
        name,score = row
        score = int(score)
        
        if score > maxsc :
            maxsc = score
            top_stud = name
# print(top_stud , maxsc)



#  Implement a program that reads a text file and counts the
# number of words and lines in it
with open("f2.txt" , "r") as f:
    info = f.read()
    li = info.split(" ")
    print("number of words = " , len(li))
with open("f2.txt" , "r") as f:
    count = 0
    i = 1
    while i == "  ":
        f.readline()
        count += 1
        print("number of lines = " , count) 




#  Create a function that takes a list of sentences and writes
# them to a new text file, each on a new line
a = " this is first line"
b = " this is second line "
c = " this is the third line "
li = [a,b,c]
def wrfu(l):
    with open("new.txt" , "w") as f :
        for sen in l:
            f.write(f"{sen}\n")
# wrfu(li)       


#  Given a CSV file with employee details (name, age,
# salary), calculate the average salary of all employees
import csv
with open("emp.csv" , "r+") as f:
    i = csv.reader(f)
    next(i)
    salar = []
    for row in i:
        name,age,salary = row
        salar.append(salary)
    sum = 0
    for s in salar:
        sum += int(s)
    avg = sum / 3
    # print(sum)
    # print(avg)



#  Write a program that reads a CSV file and finds the total
# sales revenue for a specific product



#  Given a text file with a list of numbers, write a function
# that finds the sum of all numbers in the file
def findsum():
    with open("numbs.txt" , "r") as f:
        data = f.read()
        d = data.split(",")
        sum = 0
        for num in d:
            sum += int(num)
        print("sum of all nums in file = " , sum)
# findsum()

#  Implement a program that reads a CSV file and generates
# a bar chart to represent the data using Matplotlib



#  Write a function that reads a JSON file and extracts
# specific information from it



#  Given a CSV file with temperature data for each day of
# the week, find the average temperature for each day.
import csv
with open("temp.csv" , "r") as f:
    tempD = csv.reader(f)
    next(tempD)
    sum = 0
    tempe = []
    for row in tempD:
        temp = row
        for temp in row:
            tempe.append(temp)
    print(tempe)   
    for i in tempe:
        sum += int(i)
    print("sum = " , sum)
    print("average temp = " , sum/7)
