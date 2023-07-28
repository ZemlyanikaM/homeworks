matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]


def check_matrix(matrix) -> bool:
    if len(matrix) == len(matrix[0]):
        return True
    else:
        return False


def transpone_matrix(matrix):
    transponed_matrix = [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]
    print("Transponed metrix:\n", transponed_matrix)


print("The input matrix:\n", matrix)
if check_matrix(matrix):
    transpone_matrix(matrix)
else:
    print(" The Input maxrix size is wrog!\n", matrix )
