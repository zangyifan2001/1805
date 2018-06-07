import time
print("　　　　　　　　　　欢迎使用取款机")

a = input("输入您的姓名:")

print("欢迎%s先生"%a)

int(input("输入您的账号(可支持qq用户):"))
int(input("输入您的账号密码:"))

print("　　　　　　　　　　　正在登录")

time.sleep(1)

c = 8000 

print("%s先生，您卡上余额为:%d"%(a,c))

d = int(input("请输入您的取款金额:"))

print("　　　　　　　　　　　取款成功")

e = (c-d)

print("卡剩余额:%d元"%e)

