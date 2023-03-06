import time
from time import time


user_num1 = int(input())

user_num2 = int(input())


if user_num1 < 0:
    print("user_num1 is negative.")


user_num2 = 4 if user_num2 > 14 else 10

if user_num2 > 14:
    user_num = 4
else:
    print("user_num2 is less than or equal to 14.")


print('user_num2 is', user_num2)