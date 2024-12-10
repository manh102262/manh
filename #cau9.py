#cau9
x,n = map(int,input().split())
S = 1
for i in range (1, n + 1):
    S += x ** i
    print(S)