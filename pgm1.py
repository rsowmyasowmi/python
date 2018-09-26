def power(b,exp):
if(exp==1):
    return(b)
if(exp!=1):
    return(b*power(b,exp-1))
b=int(input("Enter b: "))
exp=int(input("Enter exponential value: "))
print("Result:",power(b,exp))
