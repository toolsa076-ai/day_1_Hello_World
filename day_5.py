num = int(input("enter your table number "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
num = int(input("enter your table number"))
for i in range (1,20):
      print(f"{num} x {i} = {num * i}")   
import math
print(math.sqrt(12))
print(math.pi)      
import random
age = random.randint(3,9)
print(age)
import random
secret = random.randint(1,10)
guess = int(input("guess the number between 1 and 10"))
if guess == secret:
     print("you are right")
else:
     print("you are wrong")