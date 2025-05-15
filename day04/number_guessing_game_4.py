import random

num = random.randint(1, 20)

debug_mode = False

while True:
        if debug_mode == True:
         print ("Debug: The hidden number is,", num)
        Guess = input("Guess a whole number between 1 and 20: ")
        if Guess == "s":
         print ("The hidden number is: ", num)
         break
        if Guess == "X":
         print ("Game over")
         break
        if Guess == "d":
         debug_mode = not debug_mode
         print ("Debueg mode: ", "ON" if debug_mode else "OFF")
         continue
        else:
          Guess = int(Guess) 
        if Guess > num:
         print ("Your guess is too high, try again.")
        elif Guess < num:
         print ("Your guess is too low, try again.")
        else:
         print ("Your guess is correct")   
         break