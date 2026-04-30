import math

x = float(input("side 1: "))
y = float(input("side 2: "))

hypo = math.sqrt(pow(x,2) + pow(y, 2))

print(round(hypo, 2))