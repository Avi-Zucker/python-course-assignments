import random

num = random.randint(1, 20)


while True:
        Guess = input("Guess a whole number between 1 and 20: ")
        if Guess == "X":
         print ("Game over")
         break
        else:
          Guess = int(Guess) 
        if Guess > num:
         print ("Your guess is too high, try again.")
        elif Guess < num:
         print ("Your guess is too low, try again.")
        else:
         print ("Your guess is correct")   
         break