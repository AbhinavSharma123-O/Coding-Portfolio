n=int(input("Enter number"))
sum=0
count=0
for i in range (1,n+1):
    if n%i==0:
        count=count+1
        sum=sum+i
        print(i,'is a factor')
print(f"sum is {sum}")
print(f"count is {count}")
