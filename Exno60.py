nterms=int(input())
num1 = 0
num2 = 1
count = 0
l=[]
if nterms <= 0:
    print("Please enter a positive integer")
elif nterms == 1:
    print("Fibonacci sequence upto",nterms,":")
    l.append(num1)
    print(l)
else:
    print("Fibonacci sequence upto",nterms,":")
    while count < nterms:
        l.append(num1)
        nth = num1 + num2
        num1 = num2
        num2 = nth
        count += 1
print(l)
