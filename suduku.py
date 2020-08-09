#! /usr/bin/python3

matrix = [  [7,0,1,0,0,2,0,4,3],
            [0,0,6,4,0,3,0,0,0],
            [0,0,0,9,0,0,6,1,0],
            [0,1,4,7,0,0,0,0,0],
            [0,0,0,0,5,0,0,0,0],
            [0,0,0,0,0,6,1,2,0],
            [0,3,7,0,0,9,0,0,0],
            [0,0,0,6,0,7,3,0,0],
            [9,8,0,1,0,0,0,0,7]
        ]   

def possible(y,x,n):
    global matrix

    for i in range(0,9):
        if matrix[y][i] == n:
            return False
    for i in range(0,9):
        if matrix[x][i] == n:
            return False

    x0 = (x//3) * 3
    y0 = (y//3) * 3

    for i in range(0,3):
        for j in range(0,3):
            if matrix[y0+i][x0+j] == n:
                return False
    return True


def solve():
    global matrix
    for y in range(9):
        for x in range(9):
            if matrix[y][x] == 0:
                for i in range(1,10):
                    if possible(y,x,i):
                        matrix[y][x] = i
                        solve()
                        matrix[y][x] = 0
                return
    print_matrix()
    input('More ?')    

   

def print_matrix():
    global matrix
    for row in matrix:
        print(row)

print_matrix()
print('#################################')
solve()



