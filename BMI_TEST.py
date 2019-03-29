#
i = 0
while
tz=float(input('请输入您的体重(退出请按Q)：'))
sg=float(input('请输入您的身高：'))
BMI=tz/(sg*sg)
if BMI<16.5:
    print('过轻')
elif BMI<24.0:
    print('正常')
elif BMI<28.0:
    print('过重')
else:
    print('肥胖')