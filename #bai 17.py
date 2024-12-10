#bai 17
import math
x1,y1 = map(float, input().split())
x2,y2 = map(float, input().split())
x3,y3 = map(float, input().split())

AB = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
BC = math.sqrt((x3 - x2)**2 + (y3 - y2)**2)
AC = math.sqrt((x3 - x1)**2 + (y3 - y1)**2)

if AB + BC > AC and AB + AC > BC and AC + BC > AB:
    print("la tam giac")
else:
    print("khong phai tam giac")