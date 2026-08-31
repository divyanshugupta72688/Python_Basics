import datetime
import random
import math
import UserModule as U
x = datetime.datetime.now()
print(x)

y = datetime.datetime(1997, 10, 14)
print(y.strftime("%A"))

a = random.randint(1, 100)
b = random.randint(1, 100)
print(a)

l = ["heads", "tails", "maderchod"]
z = random.choice(l)
print(z)

x = max(12, 75, 41)
print(x)
print(math.floor(4.7))  # 4
print(math.ceil(4.7))   # 5

f = U.add(1, 2)
print(f)

h = U.employee["Status"]
print(h)