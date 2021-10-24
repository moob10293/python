import sys
import random

input("start? ")
numbers = [2,3,4,5,6,7,8,9,10,11,12]

random.randrange(1,10)
for x in range(100):
    firstnumber = random.randrange(2,12)
    secondnumber = random.randrange(2,12)
    print(f"what is {firstnumber} times {secondnumber}?")
    while input("answer: ") != f"{firstnumber * secondnumber}":
        print("fail, try again.")
        