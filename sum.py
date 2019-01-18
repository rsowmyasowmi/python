def sumall():
	g=int(input())
	h=[]
	sum=0
	for i in range(g):
		h.append(int(input()))
		sum+=h[i]
	print(sum);
try:
	sumall()
except:
	print('invalid');

