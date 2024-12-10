#cau 3
import math
a = float(input())
while True:
    if a == 0:
        a = float(input("nhap lai a: "))
    else:
        break
    
b = float(input())
while True:
    if b == 0:
        b = float(input("nhap lai so b: "))
    else:
        break
c = float(input())

delta = b**2 - 4 * a * c

if delta < 0:
    print("vo nghiem")
elif delta == 0:
    print("co nghiem kep x1 = x2 = ", -(b / (2 * a)) )
else:
    print("co 2 nghiem:")
    print("x1 = ", (-(b) + math.sqrt(delta))/(2*a) )
    print("x2 = ", (-(b) - math.sqrt(delta))/(2*a) )
