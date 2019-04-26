# Using python 3.6.6

import numpy as np

# Use division
# def skip_prod(input_list):
# 	total = np.prod(input_list)
# 	return [total // i for i in input_list]

# print(skip_prod([3, 2, 1]))
# print(skip_prod([1, 2, 3, 4, 5]))


# Solve it without division operator and in O(n).
# Ref. https://www.geeksforgeeks.org/a-product-array-puzzle/
# Python3 program for A Product Array Puzzle
def productArray(arr, n):

	i, temp = 1, 1

	# Allocate memory for the product array
	prod = [1 for i in range(n)]

	# Initialize the product array as 1

	# In this loop, temp variable contains product of
	# elements on left side excluding arr[i]
	for i in range(n):
		prod[i] = temp
		temp *= arr[i]

	# Initialize temp to 1 for product on right side
	temp = 1

	# In this loop, temp variable contains product of
	# elements on right side excluding arr[i]
	for i in range(n-1, -1, -1):
		prod[i] *= temp
		temp *= arr[i]

	# Print the constructed prod array
	for i in range(n):
		print(prod[i], end =" ")


# Driver Code
arr = [10, 3, 5, 6, 2]
n = len(arr)
print("The product array is: ")
productArray(arr, n)

# This code is contributed by mohit kumar