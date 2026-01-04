nums = [21, 21, 21]
total_sum = 0
for num in nums:
    divisors = []
    for j in range(1, num + 1):
        if num % j == 0:
            divisors.append(j)
    if len(divisors) == 4:
        total_sum += sum(divisors) 
print(total_sum)
