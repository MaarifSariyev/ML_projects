import numpy as np

def Levenshtein_distance(string_1,string_2):

    size_a = len(string_1) + 1
    size_b = len(string_2) + 1

    matrix = np.zeros((size_a,size_b))

    for i in range(size_a):
        matrix[i,0] = i

    for j in range(size_b):
        matrix[0,j] = j

# print("Matrix zeros :\n",matrix)

    for i in range(1,size_a):
        for j in range(1,size_b):
            if string_1[i-1] == string_2[j-1]: #check if the characters are same
                matrix[i,j] = min(matrix[i-1,j-1], matrix[i,j-1]+1, matrix[i-1,j]+1)
            else:
                matrix[i,j] = min(matrix[i-1, j-1]+1, matrix[i-1,j]+1, matrix[i,j-1]+1)
    print("Leveshtein distance matrix:\n", matrix)

# Define 2 strings:

string_1 = input("enter the first word:")
string_2 = input("enter the second word:")

#Let's call the function
Leveshtein_distance(string_1,string_2)
