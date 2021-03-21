# dice
import random

number = int(input("Enter a number (1 to 6) : "))
outcome = random.randint(1, 6)

if number == outcome:
    print("Winner, it was {0}".format(outcome))
else:
    print("Loser, it was {0}".format(outcome))
