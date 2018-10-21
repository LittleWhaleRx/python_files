def zf(x):
    n = len(x)
    m = 0
    l = 0
    if n < 2:
        print("输入长度不能小于2")
    while m <= n//2:
        if x[0+m] != x[-1-m]:
            print('非回数')
            break
        else:
            l += 1
            if l == n//2:
                print('是回数')
        m += 1
y = '123212'
zf(y)