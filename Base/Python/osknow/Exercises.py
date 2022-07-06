# -*-encoding:utf-8-*-

import string
import random

length = 4
al = string.ascii_letters
di = string.digits
print(al, di)
li = random.sample(al + di, length)
print(li)