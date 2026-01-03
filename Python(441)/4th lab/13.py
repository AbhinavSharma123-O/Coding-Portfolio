n=int(input("ENter"))
count=0
Sum=0
for i in range (1,n+1):
    if n%i==0:
        count+=1

if count==2:
    print("PRime")
else:
    print("Not prime")
