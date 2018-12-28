def round( n1 ): 
a = (num1 // 10) * 10
b = a + 10
return (b if num1 - a > b - num1 else a) 
num1 = 4722
    print(round(num1)) 

