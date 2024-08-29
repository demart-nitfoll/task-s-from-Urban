def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([value] * m)
    return matrix
n, m, value = int(input('Введите количество строк и столбцов, а также чем их заполнить через enter и я создам такую матрицу: \n')), int(input()), int(input())
print(get_matrix(n,m, value))