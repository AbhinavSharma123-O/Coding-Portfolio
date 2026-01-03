import numpy as np

def reshape_array(arr, new_shape):
    try:
        reshaped = arr.reshape(new_shape)
        print("Reshaped Array:\n", reshaped)
    except ValueError:
        print("Error: Cannot reshape array with the given dimensions.")

arr = np.arange(1, 13)
print("Original Array:", arr)

reshape_array(arr, (4, 3))  
reshape_array(arr, (2, 6))
