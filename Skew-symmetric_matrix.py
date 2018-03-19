"""
Input: A square matrix as a list of lists with integers.
Output: If the matrix is skew-symmetric or not as a boolean.
Example:
symmetric([
    [ 0,  1,  2],
    [-1,  0,  1],
    [-2, -1,  0]]) == True
symmetric([
    [ 0,  1, 2],
    [-1,  1, 1],
    [-2, -1, 0]]) == False
"""
def symmetric(matrix):
    start, count = 0, 0
    for i in range(len(matrix)):
        # check diagonal
        if matrix[i][start] != 0:
            return False
        else:
            # sum row win 0
            for row in range(start, len(matrix[i])):
                count += matrix[i][row]
            # sum column win 0
            for col in range(start, len(matrix)):
                count += matrix[col][start]
            start += 1
            if count != 0:
                return False
    return True

# test
print(symmetric([[0,1,2,1],[-1,0,3,3],[-2,-1,0,3],[-3,-3,-3,0]]))
print(symmetric([[ 0,  1,  2],[-1,  0,  1],[-2, -1,  0]]))