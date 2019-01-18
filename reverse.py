def rev():
	n2=int(input())
	rev=0
	while(n2!=0):
		r2=n2%10
		rev=rev*10+r2
		n2//=10
	print(rev)
try:
	rev()
except:
	print('invalid')
