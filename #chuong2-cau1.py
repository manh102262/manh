#chuong2-cau1
a = int(input())
while True:
    if a == 0:
        print("nhap so khac khong 0: ")
        a = int(input())
    else:
        break
b = int(input())

print("nghiem cua phuong trinh la x = ", (-b / a))