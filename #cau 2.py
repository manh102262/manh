#cau 2
a,b = map(int,input().split())
if a == 0:
    if b == 0:
        print(VSN)
    else:
        print(VN)
if a > 0:
    print("x > ", -b/a)
else:
    print("x < ", -b/a)