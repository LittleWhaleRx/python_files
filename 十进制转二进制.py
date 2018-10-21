def gcd(x):
    if x == 1:
        print(x,end = ' ')
    else:
        y = x%2
        gcd(x//2)
        print(y, end=' ')
x = int(input('请输入要转换成二进制的十进制数字：'))
print('转换为二进制为：',end = ' ')
gcd(x)