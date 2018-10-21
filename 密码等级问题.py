# 密码安全性检查代码
#
# 低级密码要求：
#   1. 密码由单纯的数字或字母组成
#   2. 密码长度小于等于8位
#
# 中级密码要求：
#   1. 密码必须由数字、字母或特殊字符（仅限：~!@#$%^&*()_=-/,.?<>;:[]{}|\）任意两种组合
#   2. 密码长度不能低于8位
#
# 高级密码要求：
#   1. 密码必须由数字、字母及特殊字符（仅限：~!@#$%^&*()_=-/,.?<>;:[]{}|\）三种组合
#   2. 密码只能由字母开头
#   3. 密码长度不能低于16位
sympols = r'''~!@#$%^&*()_=-/,.?<>;:[]{}\|'''
number = '0123456789'
zm = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
mm = input('请输入您的密码：')
long = len(mm)
l = 0
if mm.isspace() or long == 0:
    mm=input('密码不能为空，请重新输入：')
for i in mm:
    if i in sympols:
        l += 1
        break
for i in mm:
    if i in zm:
        l += 1
        break
    else:
        l = 5
        break
for i in mm:
    if i in number:
        l += 1
        break
    else:
        l = 6
        break
if long <= 8:
    ll = 1
if 8 < long <16:
    ll = 2
if 16 <= long:
    ll = 3
print('您的密码等级为：',end = '')
if (l == 10 or l == 11) and ll == 1:
    print('低')
elif ll == 3 and l == 3:
    print('高')
elif l == 6 or l == 7:
    print('中')
else:
    print('有问题！')