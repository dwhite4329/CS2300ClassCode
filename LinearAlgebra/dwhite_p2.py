'''
Devon White
CS2300-001
Programming Assignment #1 - part2
Due: Sunday February 4, 2024
'''

# Part 2 - Use created files and compute matrix arithmetic

# Get user input
input1 = input("Enter first matrix you'd like to add (e.g. mat1,mat2): ").lower()
input2 = input("Enter second matrix you'd like to add: ").lower()

# Name in file in/out
name = "dwhite"

# File name to be found
file1 = f"{name}_{input1}.txt"
file2 = f"{name}_{input2}.txt"


# Create file path to selected file
file_path = "/Users/devonwhite/Desktop/Github/CS2300-Classwork/Programming Assignments/Program1/"
finalFile1 = f"{file_path}{file1}"
finalFile2 = f"{file_path}{file2}"

# Output file number for file digits of files selected
def input_mat1():
    outDigit = 1
    return outDigit

def input_mat2():
    outDigit = 2
    return outDigit

def input_mat3():
    outDigit = 3
    return outDigit

def input_mat4():
    outDigit = 4
    return outDigit

def default_mat():
    return "Unknown matrix selection"

# Matrix switch statement to obtain output digits
matrix_switch = {
    'mat1': input_mat1,
    'mat2': input_mat2,
    'mat3': input_mat3,
    'mat4': input_mat4,
}

# Create file output digit based off of user input
outputDigit1 = matrix_switch.get(input1, default_mat)()
outputDigit2 = matrix_switch.get(input2, default_mat)()


# Reading selected matrices from files 
try:
    with open(finalFile1, 'r') as file:
        matrix1 = [list(map(float, line.split())) for line in file]

    with open(finalFile2, 'r') as file:
        matrix2 = [list(map(float, line.split())) for line in file]

except Exception as e:
    print(f"Error reading matrix from '{finalFile1}': {e}")
    print(f"Error reading matrix from '{finalFile2}': {e}")

# If/Else to ensure matrices can be added
if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
    print("ERROR: Matrices cannot be added!")
    print("REASON: Mismatch dimensions")

else:
    result_matrix = [[0.0] * len(matrix1[0]) for _ in range(len(matrix1))]

    #specified output folder
    output_folder = "/Users/devonwhite/Desktop/Github/CS2300-Classwork/Programming Assignments/Program1"


    # outputFile name
    outputFile = f"{output_folder}/{name}_p2_out{outputDigit1}{outputDigit2}.txt"

    # Adding the two matrices together
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            result_matrix[i][j] = matrix1[i][j] + matrix2[i][j]

    # Print results to a file
    with open(outputFile, 'w') as file:
        for row in result_matrix:
            file.write('  '.join(map(str, row)) + '\n')
