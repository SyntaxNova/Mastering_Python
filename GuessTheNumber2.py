import random
randomNum = random.randint(0,100)

def GuessTheNumber(num):
    while True:
        n = (input("Guess the between 0 to 100 or quit(Q)  = "))
        if n == "Q":
            return
        n = int(n)
        if n < 0 or n > 100:
            print("please guess number between 0 to 100 ")
        elif n == num :
            print("Correct Number guessed !")
            return
        elif(n > num):
            print("You guessed big number")
        elif(n<num):
            print("You guessed small number")
            
GuessTheNumber(randomNum)