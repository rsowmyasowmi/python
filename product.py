a1=input("enter the number")
if(a1<=100000000000):
    b1=len(a1)
    i=0
    f1=1
    while i<int(b1):
        f1=f1*int(a1[i])
        i+=1
    print(f1)
