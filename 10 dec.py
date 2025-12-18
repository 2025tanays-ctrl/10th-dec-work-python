# """
# import numpy as np

# arr = np.array([1,2,3,4])

# print(arr)
# """
# """""
# import numpy as np 

# arr = np.array([1,2,3,4,], dtype='i1')
# arr1 = np.array([1,2,3,4,], dtype='i2')
# arr3 = np.array([1,2,3,4,], dtype='i4')


# print(arr)
# print(arr.dtype)
# print(arr1.dtype)

# print(arr3.dtype)
"""""
import numpy as np

arr = np.array(["helloooo","o"], dtype='a')
print(arr.dtype)
"""
"""""
import numpy as np

arr = np.array([1,0,3])

newarr = arr.astype(bool)

print(newarr)
print(newarr.dtype)
"""""
"""""
import numpy as np 

arr = np.array([1,2,3,4,5])
x = arr.copy()
arr[0] = 42

print(arr)
print(x)
"""""
"""""
import numpy as np 

arr = np.array([1,2,3,4,5])
x = arr.view()
arr[2] = 123

print(arr)
print(x)
"""""
import numpy as np 

arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])

newarr = arr.reshape(6, 2)

print(newarr)