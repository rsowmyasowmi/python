def lex():
	m=input()
	n=list(m)
	n.sort()
	c=''.join(n)
	print(c);
try:
	lex()
except:
	print('invalid');
