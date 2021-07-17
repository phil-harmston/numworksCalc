
import random
again = True
while again:
  x = input("Enter number 1: ")
  y = input("Enter number 2: ")
  x = int(x)
  y = int(y)

  if x > y:
    z = y
    x = y
    y = z

  randomNumber = random.randint(x, y)
  print(randomNumber)
  quit = input("Do you want another random 'y' to get another")
  if quit != "y":
    again = False