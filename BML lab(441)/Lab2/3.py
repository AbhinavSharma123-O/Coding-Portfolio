#Reshape 1D array into 2Dand 3D matrix
import numpy as np
def reshape_array(arr, new_shape):
    try:
        reshaped = arr.reshape(new_shape)
        print("Reshaped Array:", reshaped)
    except ValueError:
        print("Error:")
arr = np.arange(1, 13)
print("Original Array:", arr)
reshape_array(arr, (4, 3))  

