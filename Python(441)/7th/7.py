import numpy as np
arr=np.array([[1,2,3],[4,5,6]])
print("2d array is ",arr)
print("array elements")
for i in range (arr.shape[0]):
    for j in range(arr.shape[1]):
        print(arr[i][j],end='')
    print()
arr1=np.array([[1,2,3],[4,5,6]])
arr2=np.array([[2,4,6],[3,6,9]])
res=arr1+arr2
multi=arr1*arr2
print(res)
print(multi)
