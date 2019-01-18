def isogram():
	n=input()
	x=list(n)
	r=[]
	for i in x:
		if not i in r:
			r.append(i)
	if len(x)==len(r):
		print('yes');
	else :
		print('no');
try:
	isogram()
except:
	print('invalid');
