import random
cp = random.randint(1,3)
i = 0
while i < 3: 
	a = input("开始猜拳\n请输入1剪刀或2石头或3布:")

	if (a==1 and cp==3) or (a==2 and cp==1) or (a==3 and cp==2):
		print("我赢了＼（＾ｏ＾）／,电脑就是个垃圾哈哈哈哈哈")
	elif cp == a :
		print("平局，呦呦呦～，有意思！")
	else:
		print("不服再战！啊啊啊＾（＊￣（ｏｏ）￣）＾")
	i +=1
