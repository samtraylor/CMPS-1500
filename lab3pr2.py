#Sam Traylor, Feb 11
#Purpose of program is to generate licence plate numbers

import random

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
nums = "123456789"

def licensePlate(num_letters):
    plate = ""
    while num_letters > 0:
        plate += random.choice(alpha)
        num_letters -= 1
    while len(plate) < 6:
        plate += random.choice(nums)
    return plate
    

