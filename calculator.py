def si():
	(p2,n2,r2)=map(int,sys.stdin.readline().split())
	sii=p2*n2*r2/100
	print(math.floor(sii))
try:
	si()
except:
	print('invalid')
