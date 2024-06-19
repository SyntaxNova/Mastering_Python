import random
import string

AllChar = string.ascii_letters + string.digits + string.punctuation

# list complrehension
result = "".join([random.choice(AllChar) for i in range(7)])
print(f"Random Password = {result}")

# using String 
password = ''
for i in range(7): # 7 is excluded
    password += random.choice(AllChar)
    
print(f"Random password = {password}")