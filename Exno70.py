def nextPowerOf2(num1): 
    count1 = 0; 
if (num1 and not(num1 & (num1 - 1))): 
  return num1 
    while( num1 != 0): 
      num1 >>= 1
      count1 += 1
      return 1 << count1; 
num1 = 0
    print(nextPowerOf2(num1)) 
