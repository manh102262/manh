#cau 12
n = int(input())
S = 0
x = 1
for i in range(1, 2 * n + 2, 2): 
    x = 1 
    for j in range(1, i + 1): 
        x *= j
    S += x

print(S)