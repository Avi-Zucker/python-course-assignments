import random

num = random.randint(1, 20)

Guess = int(input("Guess a whole number between 1 and 20: "))

if Guess == num:

   print ("Your guess is correct")

elif Guess > num:

   print ("Your guess is too high")

else:

   print ("Your guess is too low")