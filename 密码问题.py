n = 3# 三次输入机会
while n<=3:
    i=input("请输入密码：")
    #输入正确，程序结束
    if i == 'zhimakaimen':
        print('密码正确进入程序。。。')
        break
    else:
        #检测输入字符中是否含有‘*’，如果有则不扣除输入次数
        if '*' in i:
            print('密码中不能含有"*"，请重新输入（剩余'+str(n)+'次机会）')
        #如果没有‘*’，扣除输入次数
        else:
            n -= 1
            print("密码输入错误，还有"+ str(n) +"次机会，请重新输入")