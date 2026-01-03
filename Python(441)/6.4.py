'Create New list only with prime numbers:'
nums = [5, 3, 8, 9, 7,2, 4, 6]
p=[]
for i in nums:
    prime=0
    for j in range(2,i):
        if i%j==0:
            prime=1
    if prime==0:
        p.append(i)
print(f'the prime list is {p}')
        

