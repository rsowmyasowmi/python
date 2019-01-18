import sys
def cuboid():
	l3,b3,h3=map(int,sys.stdin.readline().split())
	print(l3*b3*h3)
try:
	cuboid()
except:
	print('invalid')
