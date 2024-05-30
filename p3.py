# list and tuples
list = [1,2,3,4,5,6]
# list slicing list[1:2] returns [2,3]
# list are mutable but strings are not in python

# list functions 

# list.append(value) 
# adds value at the end 

# sort() asc 
# sort(reversed=True) desc order

# reverse() return reversed str

# insert(idx , el) adds an element at index

# remove(value) removes element from list for first occurence only

# pop(idx) removes element from i th index

# tup = (1,2,3,4,5,6,7,8,9)
# tup.index(2) returns first occurence if the value
# tup.count(val) retyrns total no of occurences
# slicing is posible


#qns 1
# tup = []
# tup.append(input('movie1 = ')) 
# tup.append(input('movie1 = ')) 
# tup.append(input('movie1 = ')) 
# print(type(tup) , tup)

# plist = [1,2,3,2,1]
# oplist = plist.copy
# oplist.reverse()

# if(plist == oplist):
#     print('palindrom')
# else:
#     print('not')

tup =(1,1,2,2,3,3,4,5,6,7,8,9,0)
print(tup.count(1))