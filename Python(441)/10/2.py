import numpy as np
arr1=np.empty(3,dtype=int)
print("Enter 1st arr")
for i in range(3):
    val1=int(input("Enter the val of"))
    arr1[i]=val1
arr2=np.empty(3,dtype=int)
print("Enter 2nd arr")
for i in range(3):
    val2=int(input("Enter the val of"))
    arr2[i]=val2
print(arr1)
print(arr2)
i=0
while(i<=2):
    print(arr1[i]+arr2[i])
    print(arr1[i]-arr2[i])
    print(arr1[i]*arr2[i])
    print(arr1[i]/arr2[i])
    i=i+1
    
    
    
