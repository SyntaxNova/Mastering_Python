with open("practice.txt" , "w")as f:
    f.write("Hi everyone\nwe are learning file/IO \nusing java\ni like programming in java")
    
with open("practice.txt" , "r") as f:
    data = f.read()
    
def replaceFunc(d):
    newD = d.replace("java" , 'Python')
    return newD
# print(replaceFunc(data))
newD = replaceFunc(data)

with open("practice.txt" , "w+") as f:
    f.write(newD)
    
# with open ("practice.txt" , "r+") as f:
#     data = f.read()
#     if data.find("learning") != -1 :
#         print("exist")
#     else:
#         print("not found")

def checkLine():
    word = "learning"
    data  = True
    line = 1
    with open("practice.txt" , "r+") as f:
        while data:
            d = f.readline()
            if word in d:
                print("line no = " , line)
                return
            line += 1
    return -1
# print(checkLine())
# checkLine()

with open("n.txt" , "w") as f:
    f.write("1,2,3,4,5,6,7,8,9")

def check_count():
    with open("n.txt" , "r") as f :
        d = f.read()
    nums = d.split(",")
    count = 0
    for (char) in nums:
        if int(char) % 2 == 0 :
            count += 1
    print("coint for even = " , count)
# check_count()