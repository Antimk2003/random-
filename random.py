import random
for i in range(5):
    random_number = random.randint(1,20)
    print(" random number  :",random_number)

print("___________random number_____________________")

import numpy as np

arr = np.random.randint(1,10)

print("random number :",arr)

print("_____________random password_____________________")

import random
lower_case = "abcdefgijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
symbols = "@#$%&*/\?|"

use_for = lower_case+upper_case+number+symbols
length_for_pass = 8

password = "".join(random.sample(use_for,length_for_pass))
print(password)