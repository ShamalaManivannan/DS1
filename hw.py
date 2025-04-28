import numpy as np



matrix_a = np.array([2,3,6,7,8])
matrix_b = np.array([1,2,4,8,10])

operation = input("Enter operation,1 for addition, 2 for subtraction, 3 for break the program: ")
while True:
    if operation == '1':
        result = matrix_a + matrix_b
        print("Result of Addition:")
        print(result)
    elif operation == '2':
        result = matrix_a - matrix_b
        print("Result of Subtraction:")
        print(result)
    elif operation == '3':
        break
    else:
        print("Invalid operation.")