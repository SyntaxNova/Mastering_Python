strs1 = [ "apple" , "banana" , "cherry" , "jackfruit" , "blueberry" , "idvcdf" , "ofdvfd"]
name = "atharva"

# %' Given a list of words, concatenate them into a single
# string separated by spaces
def str_space(list_words):
    for char in list_words:
        print(char , end = " ")
    return
# str_space(strs1)

# ' Create a function to reverse a given string
def reversestr(s):
    return s[::-1]
# print(reversestr(name))



#  Write a program that takes a sentence as input and
#  counts the number of words in it
def sentence_count ():
    # to find number of whole words in sentence
    sentence = input("sentence = ")
    return sentence.count(" ")+1
    # Alternative way to count letters and spaces:
    # sentence.split()
    # count = len(sentence)
    # return count
# print(sentence_count())




#  Implement a function that checks if a given string is a
#  pangram (contains all letters of the alphabet)
def pangram():
    p = input("pangram = ")
    pl = p.lower()
    alpha = set("abcdefghijklmnopqrstuvwxyz")
    return alpha.issubset(pl)
# print(pangram())


# Given a string, write a function to remove all vowels from
# it and return the modified string
def remove_vowel():
    str1 = input("str = ")
    vowels = ("aeiou")
    new = []
    for char in str1 :
        if char not in vowels:
             new.append(char)
    finallist = ''.join(new)    # thing to remeber
    return finallist  
# print(remove_vowel())


#  Write a Python program to find the length of the longest
#  word in a sentence

def longestWord():
    sentence = "hello how are you, i am fine thank you"
    words = set(sentence.split())
    count = {}
    leng = []
    for char in words:
        length = len(char)
        leng.append(length)
        count[length] = char
    leng.sort()
    print("Longest word = " , count[leng[len(leng)-1]] , leng[len(leng)-1])  
    
    # words = sentence.split()
    # maxlength = 0
    # for word in words:
    #     maxlength = max(maxlength , len(word))
    # return maxlength
# print(longestWord())
# longestWord()



#  Create a function that takes a sentence as input and
# returns the sentence in reverse order
def rev_sen():
    sentence = "hello how are you, i am fine thank you"
    str1 = sentence.split()
    rev = list(reversed(str1))
    return rev
# print(rev_sen())



#  Given a list of names, count the number of names that
# start with a vowel
def sen_vo(strs):
    count = 0
    i = 0
    for char in strs:
        if strs[i][0] in list("aeiouAEIOU") :
            count+=1
        i += 1
    return count
# print(sen_vo(strs1))


#  Write a function to remove all duplicate characters from a
# given string
def remove ():
    strs1 = set(input("str = "))
    newstr = "".join(strs1)
    print(newstr)
# remove()




# Implement a program that takes a sentence and a word as
# input and checks if the word is present in the sentence.
def checkWord():
    sentence = ("hello how are you, i am fine thank you")
    word = "i"
    setsen = sentence.split()
    for char in setsen:
        if char == word:
            print("word is present") 
    return   
# checkWord()