#  Given two lists of numbers, concatenate them into a
# single list
list1 = [1,2,3,4,5]
list2 = [6,7,8,9,0 , 1]
# print(list1+list2)


# Write a program that finds the largest and smallest
# elements in a list
max_num = max(list1)
# print(max_num)


#  Implement a function that takes a list of numbers and
# returns a new list with the squared values
def squared(nums):
    squared_vals = []
    for char in nums:
        square = char*char
        squared_vals.append(square)
    return squared_vals
# print(squared(list1))


#  Create a program that finds the common elements
# between two lists and stores them in a new list$
def findCom(l1 , l2):
    common = list(set(l1).intersection(set(l2)))
    return common
# print(findCom(list1 , list2))
 

#  Given a list of words, find the word with the maximum
# length and its length
words = ["asf" , "abcd" , "dvjnds" , "dfvjonf"]
def findMax(l1):
    max_length = len(max(l1 , key=len))
    return max_length
# print(findMax(words))
    

#  Write a Python program to count the occurrences of each
# element in a given list
oc = [1,1,1,2,2,3,3,3,3,3,4,5,6,5,4,6,7,8,9,9,0,0]
def occurence(l):
    dict = {}
    for element in l:
        if element in dict:
            dict[element] += 1
        else:
            dict[element] = 1
    return dict
# print(occurence(oc))


#  Given a list of names, remove all duplicate names and
# print the unique names$
names = ["atharva" , "atharva" , "arjun" , "krishna" , "krishna" , "arjun"]
def removeduplicate(li):
    name = set(names)
    print(name)
# removeduplicate(names)


#  Create a function that takes a list of strings and returns
# the list sorted by the length of the strings$
strs = ["asf" , "abcd" , "dvjnds" , "dfvjonf"]
strs.sort(key=len)
# print(strs)

# Write a program that checks if a given list is sorted in ascending order
l9 = [1,2,3,4,5,6,7,8,9]
def issort(l4):
    if l9 == sorted(l9):
        print("sorted")
    else:
        print("not sorted")
# issort(l9)


# Implement a function that takes two lists and returns their
# union (all unique elements from both lists).
ls1 = [1,2,3,4,5,6]
ls2 = [1,2,3,7,8,9,0]
def uni(l1,l2):
    print(list(set(l1) | set(l2))) 
# uni(ls1 , ls2)