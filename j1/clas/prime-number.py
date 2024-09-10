#check if a number is prime

#soloution 1
# number= int(input("please enter your number |->"))

# is_prime= True
# for i in range(2,number):
#     if number%i == 0:
#         is_prime = False
#         break
# print(is_prime)

#soloution 2
# number= int(input("please enter your number |->"))

# is_prime= True
# for i in range(2,number//2+1):
#     if number%i == 0:
#         is_prime = False
#         break
# print(is_prime)

#soloution 3
from math import sqrt
number= int(input("please enter your number |->"))

is_prime= True
for i in range(2,int(sqrt(number))+1):
    if number%i == 0:
        is_prime = False
        break
print(is_prime)