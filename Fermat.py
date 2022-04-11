from math import exp
import random

p = int(input("Give me a number: "))
a = random.randint(1,p-1)
b = a**(p-1)
if (b % p) == 1:
    print("We have a prime!")
else:
    print("Sorry, not a prime!")
