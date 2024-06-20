"""
(A little introduction to functions)
I'd like you to write a function that accepts two lists-of-lists of numbers and returns one list-of-lists with each of
the corresponding numbers in the two given lists-of-lists added together.

It should work something like this:

>> matrix1 = [[1, -2], [-3, 4]]
>> matrix2 = [[2, -1], [0, -1]]
>> add(matrix1, matrix2)
[[3, -3], [-3, 3]]
>> matrix1 = [[1, -2, 3], [-4, 5, -6], [7, -8, 9]]
>> matrix2 = [[1, 1, 0], [1, -2, 3], [-2, 2, -2]]
>> add(matrix1, matrix2)
[[2, -1, 3], [-3, 3, -3], [5, -6, 7]]

Try to solve this exercise without using any third-party libraries (without using pandas, for example).

"""


def add_matrices(matrix1, matrix2):
    # Verificamos que las dimensiones de las matrices sean iguales
    if len(matrix1) != len(matrix2) or any(len(row1) != len(row2) for row1, row2 in zip(matrix1, matrix2)):
        raise ValueError("Las dimensiones de las matrices no son iguales")

    # Inicializamos una matriz vacía para almacenar el resultado
    result = []

    # Iteramos sobre las filas de las matrices
    for row1, row2 in zip(matrix1, matrix2):
        # Sumamos los elementos correspondientes de las dos matrices
        result_row = [elem1 + elem2 for elem1, elem2 in zip(row1, row2)]
        # Añadimos la fila resultante a la matriz resultado
        result.append(result_row)

    return result


# Probamos la función con algunos valores
matrix1 = [[1, -2], [-3, 4]]
matrix2 = [[2, -1], [0, -1]]
print(add_matrices(matrix1, matrix2))  # [[3, -3], [-3, 3]]

matrix1 = [[1, -2, 3], [-4, 5, -6], [7, -8, 9]]
matrix2 = [[1, 1, 0], [1, -2, 3], [-2, 2, -2]]
print(add_matrices(matrix1, matrix2))  # [[2, -1, 3], [-3, 3, -3], [5, -6, 7]]



