import math
import os
import random
import re
import sys

try:
    n = int(input("Enter number: "))

except:
    print("Invalid input")

else:

    if 0 < n <= 100:
        if n % 2 == 1:
            print("Weired")

        elif n % 2 == 0 and 2 <= n <= 5:
            print("Not Weired")

        elif n % 2 == 0 and 6 <= n <= 20:
            print("Weired")

        elif n % 2 == 0 and n > 20:
            print("Not weired")

    else:
        print("number is out of range")




