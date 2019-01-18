a1=int(input("enter th:e n"))
b1=[]
for i in range(0,a1):
    c1=int(input("enter the input"))
    b1.append(c1)
for i in range(0,a1):
    if(b1[i]!=i+1):
        print(i+1)
