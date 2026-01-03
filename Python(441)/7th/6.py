import numpy as np
arr=np.empty(5,dtype=int)
print("Enter 5 elements")
for i in range(5):
    val=int(input(f"enter element {i+1}:"))
    arr[i]=val
print("Final Numpy array",arr)
