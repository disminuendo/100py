def matriz_bidimensional (x, y):

    matriz=[[0 for col in range(y)] for row in range(x)]

    for row in range (x):
        for column in range (y):
            matriz[row][column] = row*column
    return matriz
    

print(matriz_bidimensional(3,5))