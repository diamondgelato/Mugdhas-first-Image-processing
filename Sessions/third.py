import numpy as np
import cv2

new = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

array = np.array ([1, 2, 3, 4])
array2 = array [0:2:1]                      # 'slicing' array: [ start_index : stop_index : step]
array3 = array [3:0:-1]                     # going in reverse
array4 = array.copy ()                      # copy array

matrix = np.array ([[1, 2, 3], [4, 5, 6], [7, 8, 9]])                       # 2 dimensional array (matrix)
matrix2 = np.array ([[1, 2], [3, 4], [5, 6]])
matrix3 = matrix2.copy()

multiplied = np.matmul (matrix, matrix2)                                    # multiplies 2-D arrays like they are matrices

#np.any
#np.all

#print (np.max (array))                                                     # returns max element
#print (np.argmax (array))                                                   # returns index of max element
print (list(zip(new)))
print (list(zip(*new)))

black = np.zeros ((500, 500), np.uint8)                                     # array with all zero elements (also a black image)
white = 255 * np.ones ((500, 500), np.uint8)                                # array with all 1 (* 255, because premultiply) elements

whitenoise = np.random.randint (0, 255, (500, 500), np.uint8)               # random greyscale image
justnoise = np.random.randint (0, 255, (500, 500, 3), np.uint8)             # random coloured image

#cv2.imshow ('white', justnoise)
#cv2.waitKey (0)

# print (array2)
