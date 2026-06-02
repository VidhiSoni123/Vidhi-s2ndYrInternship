# 1) Replace Nan with 0 and Interchange 3 rows and 3 columns of 2D array [[6, -8, 73, -110], [np.nan, -8, 0, 94]] 

import numpy as np
arr=np.array([[6, -8, 73, -110], [np.nan, -8, 0, 94]]) 
arr2 = np.nan_to_num(arr, nan=0)
print(arr)
print(arr2)

#*interchange
#print(arr.T)
import numpy as np

a=np.array([[6, -8, 73, -110],
            [np.nan, -8, 0, 94],
            [1,2,3,4],
            [5,6,7,8]])

print("Original Array:")
print(a)

a[[0,1,2],:] = a[[2,0,1],:]
print("\nAfter Row Interchange:")
print(a)

a[:,[0,1,2]] = a[:,[2,0,1]]
print("\nAfter Column Interchange:")
print(a)

#*2) Move axes of 3D array to new positions

#* 3) Replace NaN values with average of columns 
arr=np.array([[6, -8, 73, -110], [np.nan, -8, 0, 94]]) 
avg=6
arr2=np.nan_to_num(arr,nan=avg)
print(arr2)



# 4) Replace negative value with zero in numpy array using replace

a=np.array([1,-2,5,6,-7])
a1=np.place(a, a < 0, 0)
print(a)
print(a1)
 
#* 5) Study the following program 
import numpy as np 
#create a numpy 1d-arrays 
arr1 = np.array([3, 4]) 
arr2 = np.array([1, 0]) 
# find average of NumPy arrays
avg = (arr1 + arr2) / 2 
print("Average of NumPy arrays:\n", avg) 


# -> Calculate average mean median mode values of two NumPy 2d-arrays 
#Mean
print("Mean =", np.mean(avg))

# Median
print("Median =", np.median(avg))


# 6) Solve the following equation using linalg() and inverse Matrix method 
# x - 2y + 3z = 9 
# -x + 3y - z = -6 
# 2x - 5y + 5z = 17

arr1=np.array([[1,-2,3],[-1,3,-1],[2,-5,5]])
arr2=np.array([9,-6,17])
res=np.linalg.solve(arr1,arr2)
print("result",res)

#using inverse method
arr1=np.array([[1,-2,3],[-1,3,-1],[2,-5,5]])
arr1inv=np.linalg.inv(arr1)
res=np.dot(arr1inv,arr2)
print(res)

#7) Using "Customizing Matplotlib Visualizations" discussed in Numpy session4 notes plot graph to compare your at least 2 semester result

import numpy as np
import matplotlib.pyplot as plt
x=np.array(["Sem1","Sem2","Sem3","Sem4"])
y=np.array([8.97,9.27,8.53,8.10])
plt.scatter(x, y, color='red', alpha=0.7)
plt.title('Scatter Plot of Semester marks')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()
