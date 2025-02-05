'''
Devon White
CS2300-001
Programming Assignment #1
Due: Sunday February 4, 2024
'''
import numpy as np

# Part 1 - 2D arrays
# Matrices dimensions
Devon = 5
White = 5

# Matrix1 rows = last name value; cols = first name value
mat1 = np.zeros((White, Devon), dtype = int)

# Counter to assist with iterating
counter = 1

# Nested for loops to iterate through cols and rows
# Also to place values in matrix location
for col in range(mat1.shape[1]):
    for row in range(mat1.shape[0]):
        mat1[row, col] = counter
        counter += 1

print(mat1)


# Matrix2 rows = last name value; cols = first name value
mat2 = np.zeros((White, Devon), dtype = int)

# Initialize first value
mat2FirstValue = 2

# Nested for loops to iterate through matrix and initialize values
for row in range(mat2.shape[0]):
    for col in range(mat2.shape[1]):
        mat2[row, col] = mat2FirstValue
        mat2FirstValue = mat2FirstValue + 3

print(mat2)


# Matrix3 rows = 2, cols = 4
mat3 = np.zeros((2,4), dtype = int)

# Initialize first value
mat3Start = 10

# Matrix iteration and initialization
for col in range(mat3.shape[1]):
    for row in range(mat3.shape[0]):
        mat3[row, col] = mat3Start
        mat3Start = mat3Start + (-2)

print(mat3)


# Matrix4 rows = 4, cols = 2
mat4 = np.zeros((4,2), dtype = float)

# Initialize first value
mat4Start = (-6)

for row in range(mat4.shape[0]):
    for col in range(mat4.shape[1]):
        mat4[row, col] = mat4Start
        mat4Start = mat4Start + 1.5

print(mat4)

