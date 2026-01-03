count=0
Sum=0
for i in range (1,11):
    if i%2==0:
        count+=1
        Sum=Sum+i
        print(i,"is even")
print(count)
print(Sum)
