'''
## Questions to be done during the lab:
1. Create a (4 x 2) integer array and print it's attributes
2. Create an array of dimension (1,10) and sort it in ascending and descending order
3. Convert an 1D array [1 2 3 4 5 6 7 8 9] to 2D array [[1 2 3], [4 5 6], [7 8 9]]
4. Stack two arrays of any size horizontally and vertically
5. Create two array of same size and find commom elements
6. Create a 2D array of 5 by 5 and find the min and max values from each row and each column
7. Create an array of size 100 and  compute the mean, median, standard deviation. 
8. Normalize a 5x5 random matrix 
9. Consider an array of dimension (4,4,3), how to mulitply it by an array with dimensions (4,4)?
'''
from numpy.random import randint
import numpy as np
import matplotlib.pyplot as plt

##############
# Question 1 #
##############
print('\n# Question 1 #')
int_array = np.array([[randint(100) for _ in range(2)] for _ in range(4)])
print(int_array)
print(int_array.shape)


##############
# Question 2 #
##############
print('\n# Question 2 #')
int_array = np.array([randint(100) for _ in range(10)])
print(int_array)
print(f' Ascending order: {np.sort(int_array)}')
print(f' Ascending order: {-np.sort(-int_array)}')


##############
# Question 3 #
##############
print('\n# Question 3 #')
d1_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
d2_array = d1_array.reshape(3,3)
print(f'1D array+')
