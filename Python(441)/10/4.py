import numpy as np
arr1=np.empty(3,dtype=int)
print("Enter 1st arr")
for i in range(3):
    val1=int(input("Enter the val of"))
    arr1[i]=val1

print(np.mean(arr1))
print(np.median(arr1))
print(np.std(arr1))
print(np.var(arr1))
    
    
    
    
