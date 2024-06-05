#  Write a Python program to copy the contents of one text
# file into another2
# with open("f1.txt" , "r") as f:
#     data = f.read()
# with open("f2.txt" , "w") as f:
#     f.write(data)



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



#  Given a CSV file with employee details (name, age,
# salary), calculate the average salary of all employees



#  Write a program that reads a CSV file and finds the total
# sales revenue for a specific product



#  Given a text file with a list of numbers, write a function
# that finds the sum of all numbers in the file



#  Implement a program that reads a CSV file and generates
# a bar chart to represent the data using Matplotlib



#  Write a function that reads a JSON file and extracts
# specific information from it



#  Given a CSV file with temperature data for each day of
# the week, find the average temperature for each day.