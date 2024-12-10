#bai 10
import math

n = int(input())
x = float(input())
S = 1  
for i in range(n):
    x = math.sqrt(x) 
    S += x 
print(S)
