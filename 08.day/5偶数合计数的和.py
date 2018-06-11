a = 0
c = 0 
i = 0 
while i < 100 :
	if i%2 == 0 :
		a = a + i
	elif i%2 != 0 :
		c = c + i
	i+=1
print("%d"%a)
print("%d"%c)
print("%d"%(a+c))

