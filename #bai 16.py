#bai 16
import math
a,b,c = map(int,input().split())
if a + b > c and a + c > b and b + c > a:
    C = a + b + c
    s = C / 2

    P = math.sqrt(s * (s - a) * (s - b) * (s - c))
    
    print("la tam giac")
    print(C)
    print(P)
else:
    print("khong phai la tam giac")