import random

num = random.randint(1, 20)

debug_mode = False
move_mode = False

while True:
        if move_mode == True:
          num = max(1, min(20, num + random.choice([-2, -1, 0, 1, 2])))
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
        if Guess == "m":
          move_mode = not move_mode
          print ("Move mode: ", "ON" if move_mode else "OFF")
          continue
        if Guess == "n":
          num = random.randint(1, 20)
          print ("New game")
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
