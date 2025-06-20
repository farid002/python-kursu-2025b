"""
matrix = [
    [1, 2, 3],
    [4, 5, 6, 7],
    [8, 9]
]
İkinci daxili listin son elementini pop() ilə sil
Bütün matrix-dəki ədədləri for döngüsü ilə bir-bir çap et
"""
matrix = [
    [1, 2, 3],
    [4, 5, 6, 7],
    [8, 9]
]
matrix[1].pop()

for row in matrix:
    for element in row:
        print(element, end=" ")