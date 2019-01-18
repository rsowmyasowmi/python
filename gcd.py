import sys
def gcd2():
	(z,y)=map(int,sys.stdin.readline().split())
	while(y!=0):
		t=y
		y=x%y
		z=t
	print(z);
try:
	gcd2()
except:
	print('invalid');
