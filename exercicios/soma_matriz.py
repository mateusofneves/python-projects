a = [
    [-3, 5, 2],
    [1, 6, 4]
]

b = [
    [7, 2, 0,],
    [9, -2, 3]
]

for i in range(len(a)):
    for j in range(len(a[i])):
        b[i][j] = a[i][j] + b[i][j]

for i in b:
    print(i)
