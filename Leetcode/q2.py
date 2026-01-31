nums=[2,2]
num=[]
count=nums[0]
for i in nums:
    if i!=count:
        num.append(i)
        num.append(count)
    count=count+1
print(num)
    
