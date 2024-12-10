#cau 5
a1, b1, c1, a2, b2, c2 = map(int, input().split())

if ((a1/a2) == (b1/b2)) and ((b1/b2) == (c1/c2)):
    print("vo so nghiem")

elif ((a1/a2) == (b1/b2)) and ((b1/b2) != (c1/c2)):
    print("vo nghiem")

elif (a1/a2) != (b1/b2):
    print("co 1 nghiem")

    y = (a1 * c2 - a2 * c1) / (-a2 * b1 + a1 * b2)
    x = (c1 - b1 * y) / a1

    print("x =", x, ", y =", y)
