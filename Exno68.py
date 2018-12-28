def round( a ): 
m = (a // 7) * 7
b = m + 7
return (b if a - m > b - a else m) 
a = 4722
    print(round(a)) 
  
