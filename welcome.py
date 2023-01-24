"""
maker：whb
23/1/17
"""
import  datetime
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

print("选择你要进行的操作")
command_line='生成密码（M/m），找回密码（F/f）'
print(command_line)

while True :
    command=input("请输入字母：")
    if command.lower() in ['m','f']:
        print('请稍后')
        print('已选择'+command) #todo 已选择M ->已经选择生成/找回密码选项
        break
    else:
        print("请检查输入的选项！(m/f)")

