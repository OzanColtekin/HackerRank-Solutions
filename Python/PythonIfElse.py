import math
import os
import random
import re
import sys

number = int(input())

if (number % 2 !=0):
    print("Weird")
elif(number<6 and number >=2):
    print("Not Weird")
elif(number>=6 and number<20):
    print("Weird")
elif(number>=20):
    print("Not Weird")    
