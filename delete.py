a1=input("\nEnter the N number")
b1=input("\nEnter the K number")
c1=list(str(a1))
e1=b1
while e1>0:
    e1=e1-1
    del(c1[e1])
print(''.join(c1))

