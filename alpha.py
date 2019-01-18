def onlyint():
	p=input()
	q=list(p)
	r=''
	for i in q:
		if i.isnumeric():
			r+=i
	print(r);
try:
	onlyint()
except:
	print('invalid');
