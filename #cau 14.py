#cau 14
a =float(input())
s = 1
n = 1
x = 1
while True:
    if n > 1:
        x *=(s * n-1) *(s * n)
    t = 1 / x
    if t < a:
        break
    s += t
    n += 1
print(s)