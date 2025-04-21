import numpy as np  #importing numpy as np(aliasing)

sample_list = [1,2,3,4,5] #making a list
print(type(sample_list))  #printing the type

#converting a list to an array

sample_numpy = np.array(sample_list) #function to turn it into a array
print(type(sample_numpy))

#creating a array
arr = np.array([1,2,3,4,5,6])
print(type(arr))

#b=np.array([1,2,3],"Tharun")  #homogenous - only one type of data
#print(b)

c=np.zeros(100)  #function to print zeros
print(c)

d=np.ones(100)  #function to print ones
print(d)

arr2=np.array([1,2,3,4,5,6,7,8,9,10])
print(arr2)

#Converting the array to decimals 

arr3=np.array([1,2,3,4,5,6,7,8,9,10], dtype="f")
print(arr3)

#arr4=np.array([[1,2,3],[4,5,6],[7,8]]) #sub arrays need to have the same amount of numbers
#print(arr4)

arr5=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr5)

print("Array Dimension" ,arr5.ndim) #1D,2D,3D
print("Number of rows_col",arr5.shape) #number of rows and columns
print("Number of elements" ,arr5.size) #number of elements
print("Array size", arr5.nbytes,"bytes") #Size in bytes - 4 bytes

arr6 = np.arange(1,251) #last number is exclusive
print(arr6)

arr7 = np.arange(1,200,2) #1st=start,2nd=stop,3rd=stepsize (odd numbers)
print(arr7)

arr8 = np.arange(0,201,2) #even numbers
print(arr8)

#Random 

e=np.random.randint(1,10)
print(e)
#Prints numbers from 1 to 10 in random order
f=np.random.permutation(np.arange(1,11))
print(f)

#prints 20 rand float from 0 to 1
random_array = np.random.rand(1,20) #1st=type of dimension, 2nd=Amount of numbers
print(random_array)

random_array2=np.random.rand(5,20)
print(random_array2)

arr9=np.arange(1,26).reshape(5,5) #reshape in a 5x5 grid(5 rows and 5 columns)
print(arr9)

#task to print the numbers from 1 to 36 in factors format/grids

arr10=np.arange(1,37).reshape(2,18)
print(arr10)

arr11=np.arange(1,37).reshape(3,12)
print(arr11)

arr12=np.arange(1,37).reshape(4,9)
print(arr12)

arr13=np.arange(1,37).reshape(6,6)
print(arr13)