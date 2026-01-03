for n in range(1,10000):
    count=0
    for i in range(1,n):
        if n%i==0:
            count+=i
    if count==n:
        print("Perfect number is",n)
