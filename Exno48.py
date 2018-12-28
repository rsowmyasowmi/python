N = int(input('n numbers: '))
total_sum = 0
for n in range(N):
    numbers = float(input('Enter number : '))
    total_sum += numbers
avg = total_sum/N
print('Average of ', N, ' numbers is :', avg)
