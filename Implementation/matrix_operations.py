
def transposeMatrix(matrix):
  output = [[0] * len(matrix) for _ in range(len(matrix[0]))]
  for i in range(len(output)):
    for j in range(len(output[0])):
      output[i][j] = matrix[j][i]
  return output

def addMarrix(a, b):
  if len(a) != len(b) or len(a[0]) != len(b[0]): return
  output = [[0] * len(a[0]) for _ in range(len(a))]
  for i in range(len(a)):
    for j in range(len(a[0])):
      output[i][j] = a[i][j] + b[i][j]
    
  return output

"""
[1 2 3 4] [2 3] = [* *]
[5 6 7 8] [5 6]   [* *]
          [1 2]   
          [1 2]

2x4, 4x2.        =


"""

def multiplyMatrix(a, b):
  output = [[0] * len(b[0]) for _ in range(len(a))]
  # take columns of b and rows of 

  for i in range(len(a)): # traverse through rows
    for j in range(len(b[0])): # traverse through columns
      for k in range(len(b)):
        output[i][j] += a[i][k] * b[k][j]
    
  return output



if __name__ == "__main__":
  # Test matrices
  matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
  ]

  matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
  ]

  matrix3 = [
    [1, 2],
    [3, 4],
    [5, 6]
  ]

  matrix4 = [
    [7, 8, 9],
    [10, 11, 12]
  ]

  # Test transcribe (transpose)
  print("Original matrix1:")
  for row in matrix3:
    print(row)
  print("\nTransposed matrix3:")
  transposed = transposeMatrix(matrix3)
  print("TRANSPOSED:", transposed)

  # Test add
  print("\nMatrix1 + Matrix2:")
  added = addMarrix(matrix1, matrix2)
  print(added)

  # Test multiply (3x3 * 3x3)
  print("\nMatrix1 * Matrix2:")
  multiplied = multiplyMatrix(matrix1, matrix2)
  print(multiplied)

  # Test multiply (3x2 * 2x3)
  print("\nMatrix3 (3x2) * Matrix4 (2x3):")
  multiplied2 = multiplyMatrix(matrix3, matrix4)
  print(multiplied2)