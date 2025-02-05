'''
Devon White
CS2300-001
Programming Assignment #1 - part1
Due: Sunday February 4, 2024
'''

# Part 1 - 2D arrays
# Matrices dimensions
Devon = 5
White = 5

# Matrix1 rows = last name value; cols = first name value
mat1 = [[0] * Devon for _ in range(White)]

# Counter to assist with iterating
counter = 1

# Nested for loops to iterate through cols and rows
# Also to place values in matrix location
for col in range(Devon):
    for row in range(White):
        mat1[row][col] = counter
        counter += 1




# Matrix2 rows = last name value; cols = first name value
mat2 = [[0] * Devon for _ in range(White)]

# Initialize first value
mat2FirstValue = 2

# Nested for loops to iterate through matrix and initialize values
for row in range(White):
    for col in range(Devon):
        mat2[row][col] = mat2FirstValue
        mat2FirstValue = mat2FirstValue + 3




# Matrix3 rows = 2, cols = 4
mat3 = [[0] * 4 for _ in range(2)]

# Initialize first value
mat3Start = 10

# Matrix iteration and initialization
for col in range(4):
    for row in range(2):
        mat3[row][col] = mat3Start
        mat3Start = mat3Start + (-2)



# Matrix4 rows = 4, cols = 2
mat4 = [[0] * 2 for _ in range(4)]

# Initialize first value
mat4Start = (-6)

for row in range(4):
    for col in range(2):
        mat4[row][col] = mat4Start
        mat4Start = mat4Start + 1.5



# Print matrices to text files
name = "dwhite"

#specified output folder
output_folder = "/Users/devonwhite/Desktop/Github/CS2300-Classwork/Programming Assignments/Program1"

# Put each matrix into a list
allMatrices = [mat1, mat2, mat3, mat4]

for i, matrix in enumerate(allMatrices, start=1):
    file_name = f"{output_folder}/{name}_mat{i}.txt"
    print(file_name)

    with open(file_name, 'w') as file:
        for row in matrix:
            file.write('   '.join(map(str, row)) + '\n')
