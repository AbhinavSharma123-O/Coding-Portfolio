import numpy as np
r=3
c=3
arr=np.empty((r,c),dtype=int)
for i in range(r):
    for j in range(c):
        val=int(input('ENter kar reeeee'))
        arr[i][j]=val
print(arr)
sum=0
for i in range(r):
    for j in range(c):
        sum=sum+arr[i][j]
print(sum)

