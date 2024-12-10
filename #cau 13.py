#cau 13
n1 = int(innput())
S = 1
for i in range(1, 2 * n1 + 2, 2):
    a = 1
    for j in range(1, i + 1):
        a *= j
    s += 1 / a
print(s)
tong  = 0
for n2 in range(1, 1000):
    tong += n2
    if tong > 100:
        break