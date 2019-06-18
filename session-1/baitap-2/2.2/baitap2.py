# from turtle import *

# for z in range(6):
#     for i in range(360):
#         forward(1)
#         left(1)
#     left(130)

# mainloop()

# for i in  [1 , 8 ,2 , 10]:
#     print(i)
# N = input("N:  ")
# sum = 0 
# for z in range(0, int(N)):
#     sum = sum + z
# print(sum)

# nam_sinh = int(input("Nam Sinh:  "))
# age = 2019 - nam_sinh 
# if age < 12: 
#     print("baby")
# elif age <= 18:
#     print("teen")
# else: 
#     print("adult")

from random import randint
so = randint(0,100)
if so < 30:
    print("Rainy")
elif so < 60:
    print("Cloudy")
else:
    print ("Sunny")
print(so)