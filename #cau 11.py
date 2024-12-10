#cau 11
n = int(input())
S = 0  
x = 1
for i in range(1, n + 1):  
    x *= i  
    S += x
print(S)
