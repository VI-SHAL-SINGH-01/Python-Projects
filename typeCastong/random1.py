#this file is running chacked if it show an error then it may be import file error the you need to refress the module

import random

x = random.randint(1, 5)
print("***=> RULES OF GAME <=***")
print("1=> select a no from 1 to 5 ")
print("2=> you have three choice each  ")

print("3=> click enter to start the game ")
count=3
print("RANDOM NO. IS " ,x)
for y in range(0,3):
    print()
    count-=1
    z = input("enter your no. from 1 to 5 \n")
    if x==z:
        print("your winning probability is 0.6 and you won this game")
        break
else:
    print("you have ",count,"chances left")
print()
print("RANDOM NO. IS " ,x)
print()

t='you won at {y}'if x==z else 'better luck next time'
print(t)
    


