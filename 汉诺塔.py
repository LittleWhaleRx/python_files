def hannuo(n,a,b,c):
    '''
    汉诺塔的递归实现
    :param n: 代表几个盘子
    :param a: 代表第一个柱子,开始的塔
    :param b: 代表第二个柱子，中间过渡的塔
    :param c: 代表第三个柱子，目标塔
    :return:
    '''
    if n == 1:
        print(a, "-->", c)
        return None
    if n == 2:
        print(a, "-->", b)
        print(a, "-->",c)
        print(b,"-->",c)
        return None
    # 把n-1哥盘子，从a塔借助于c塔，挪到b塔上去
    hannuo(n-1,a,c,b)
    print(a,"-->",c)
    # 把n-1个盘子，从b塔，借助于a塔，挪到c塔上去
    hannuo(n-1,b,a,c)
a = 'A'
b = 'B'
c = 'C'
hannuo(3,a,b,c)