nums=[5,2,3,1]
n=[]
i=0
for i in range(len(nums)):
    if nums[i]<nums[i+1]:
        print(nums[i+1]+nums[i+2])
