file1 = open('data.txt', 'r')
heights = file1.readlines()

def temMaior(matrix, m, lin, col):

    up = True
    bottom = True
    left = True
    right = True

    for i in range(lin):                
        if matrix[lin][col] <= matrix[i][col]:
            up = False
            break
    
    for i in range(lin+1, m):                
        if matrix[lin][col] <= matrix[i][col]:
            bottom = False
            break
    
    for i in range(col):                
        if matrix[lin][col] <= matrix[lin][i]:
            left = False
            break
    
    for i in range(col+1, m):               
        if matrix[lin][col] <= matrix[lin][i]:
            right = False
            break

    return [up, bottom, left, right]


M = len(heights[0].strip())

MATRIX = [0]*M

for i in range(M):
    MATRIX[i] = list(map(int, list(heights[i].strip())))

total = (M * 2) + ((M-2)*2)

for i in range(1, M-1):
    for j in range(1, M-1):
        total += 1 if True in temMaior(MATRIX, M, i, j) else 0

print(total)   
