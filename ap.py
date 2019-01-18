num1=int(input("Enter any number"))
f1=0
for x in range(1,num1+1):
	if(num1%x==0):
		f1=f1+1
if(f1>2):
	print("composite")
else:
        print("Not composite")
