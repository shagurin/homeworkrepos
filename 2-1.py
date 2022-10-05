x1=int(input("Число 1: "))
x2=int(input("Число 2: "))
x3=int(input("Число 3: "))
same=0
if x1==x2:
    same=2
    if x1==x3:
        same=3
elif x1 is not x2:
    if x1==x3 or x2==x3:
        same=2
print("Совпадают: ", same)