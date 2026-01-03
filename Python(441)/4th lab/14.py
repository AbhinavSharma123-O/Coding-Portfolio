n=int(input("ENter"))
count=0
sum=0
for i in range (1,n):
    if n%i==0:
        count+=1
        sum=sum+i

if sum==n:
    print("Perfect")
else:
    print("not perfect")
