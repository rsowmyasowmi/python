def str1to2():
	x=input()
	y=list(x)
	(e,o)=('','')
	for i in range(len(y)):
		if i%2==0:
			e+=y[i]
		else :
			o+=y[i]
	print(e,o);
try:
	str1to2()
except:
	print('invalid');
