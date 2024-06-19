import random
# using while loop for better space complexity
randomNum = random.randint(0,100)

def GuessTheNumber(num):
    n = (input("Guess the between 0 to 100 or quit(Q)  = "))
    if n == "Q":
        return
    n = int(n)
    if n < 0 or n > 100:
        print("please guess number between 0 to 100 ")
        GuessTheNumber(num)
    elif n == num :
        print("Correct Number guessed !")
    elif(n > num):
        print("You guessed big number")
        GuessTheNumber(num)
    elif(n<num):
        print("You guessed small number")
        GuessTheNumber(num)
            
GuessTheNumber(randomNum)