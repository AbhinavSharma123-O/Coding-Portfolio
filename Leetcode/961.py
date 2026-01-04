nums=[5,1,5,2,5,3,5,4]
max=0
s=[]
newset=set(nums)
for i in newset:
    if nums.count(i)>max:
        max=nums.count(i)
        s.append(i)
print(s[-1])

