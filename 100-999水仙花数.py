
for i in range(100,1000):
    a = i//100
    b1 = i//10
    b = b1%10
    c = i%10
    if a**3+b**3+c**3 == i:
        print(i)
