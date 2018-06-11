import random
a = random.randint(1,100)
print("　　　　　　　　　　　　　猜猜看\n大爷快来玩啊1!!!!!")
i = 0 
while i < 10:
	c = int(input("请输入您要比较的值："))
	if a > c :
		print("大了")
	elif a < c :
		print("兄ｄｅｉ～好巧！一样大")
	else :
		print("小了")
	i += 1
