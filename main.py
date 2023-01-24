import  datetime
import random
date =datetime.datetime.now().date()
max_length=60
MESSAGE =[
    'welcome to password maker' ,
    '密码生成器',
    'author is 4usei ',
    'version =0.1' ,
    'System Time :'+str(date),
]
print('#'*max_length)
for msg in MESSAGE:
    print('{0:^{1}s}'.format(msg, max_length))
print('#'*max_length)
count=1
while True:
    command = input("随机生成密码（M/m）：")
    if command.lower() in ['m']:
        # todo 写一个函数 里面使用randon 在设置好的列表随机选择符号<-进行密码位数的设置
        n = input('for which net/为哪个网站设置：')
        while (count<=4):
            print(str(count) + ':')
            count += 1
            h1 = ['<--','!!!','^^^','$$$','###','@@@','~~~','***','+++','---']
            h2 = ['8','0','1']
            e = ['-->','!!!','^^^','$$$','###','@@@','~~~','***','+++','---']
            s = random.randint(0,9)
            p = random.randint(0,2)#todo 尝试修改成每个列表的长度再进行操作max_length
            print(h1[s]*2+h2[p]*3+'('+n+')'+h2[p]*3+e[s]*2)
        c=input('输入1返回上一级：')
        if c=='1':
            count=1
            print('已返回')
        else:
            print('退出')
            break
    else :
        print('wrong input ')


# 按间距中的绿色按钮以运行脚本。



# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
