def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append(list())               #создаем количество n списков в основном списке
        for j in range(m):
            matrix[i]= [value]*m             #создаем необходимое количество m столбцов в каждом списке
    return matrix
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)