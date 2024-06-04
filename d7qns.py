
# Given two dictionaries, merge them into a single
# dictionary
def Merge(dict1, dict2):
    return(dict1.update(dict2))
dict1 = {
    'k1' : 1,
    'k2' : 2
}
dict2 = {
    'k3' : 3,
    'k4' : 4
}
dict3 = {
    'k5' : 5,
    'k6' : 6
}
Merge(dict1 , dict2)
# print(dict1)


#  Write a program that finds the most frequent element in a
# list
listo = [1,1,1,2,3,4,5,6,7,8,9,0,2,3,4,5]
def findfre(l):
    dictc = {}
    for char in l:
        count = l.count(char)
        dictc[char] = count
    return dictc
# print(findfre(listo))


#  Implement a function that removes a key-value pair from
#  a dictionary
def removefun(dr , ke):
    dr.pop(ke)
    return dr
# print(removefun(dict1 , 'k1'))
    

# Create a program that checks if two sets have any
# elements in common
se1 = (1,2,3,4,5,6,7)
se2 = (6,7,8,9,0,1)
def checkcommon(s1 , s2):
    common = set(s1) & set(s2)
    return common
# print("common elements = " , checkcommon(se1,se2))


#  Given a list of dictionaries, find the dictionary with the
# highest value for a specific key
listOfDict = [dict1 , dict2 , dict3]


#  Write a Python program that counts the number of
# occurrences of each character in a given string using a
# dictionary
srt = "atharva"
def findocstr(l):
    s = list(l)
    dictc = {}
    for char in s:
        count = s.count(char)
        dictc[char] = count
    return dictc
# print(findocstr(srt))


#  Given two sets, find the union, intersection, and
#  difference between them
set1 = set((1,2,3))
set2 = set((3,4,5))
u = set1.union(set2)
i = set1.intersection(set2)
d = set1.difference(set2)
d1 = set2.difference(set1)
dictsets = {
    'union' : u ,
    'intersection' : i , 
    'difference in 1' : d , 
    'difference in 2' : d1
}
# print(dictsets)


#  Create a function that takes a list of dictionaries and sorts
#  them based on a specified key
dicts = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 22},
    {"name": "Charlie", "age": 23}
]
def sortlist(li, sortkey):
    return sorted(li , key=lambda x: x[sortkey])
# print(sortlist(dicts , "name"))



#  Write a program that finds the average value of all the
# elements in a list of dictionaries
dicts = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 22},
    {"name": "Charlie", "age": 23}
]
def avgOfdicts( l , k):
    total = 0
    count = 0
    for char in l :
        if k in char:
            total += char[k]
            count += 1
    if count == 0:
        return 0
    return total / count
# print(avgOfdicts(dicts , "age"))


#  Implement a function that takes a list of strings and
# returns a set of unique characters present in all strings.
strs = ["atharva" , "banana" , "apple" ]
def uniqueChar(l):
    uni = {}
    for ele in l:
        sets = set(ele)
        uni[ele] = sets
    return uni
# print(uniqueChar(strs))