def minTiles(n, m): 
      
    # base case, when area is 0. 
    if n == 0 or m == 0: 
        return 0
  
    # If n and m both are even, calculate tiles for n/2 x m/2 
    # Halfing both dimensions doesn't change the number of tiles 
    elif n%2 == 0 and m%2 == 0: 
        return minTiles(int(n/2), int(m/2)) 
  
    # If n is even and m is odd, Use a row of 1x1 tiles 
    elif n % 2 == 0 and m % 2 == 1: 
        return (n + minTiles(int(n/2), int(m/2))) 
  
    # If n is odd and m is even, Use a column of 1x1 tiles 
    elif n % 2 == 1 and m % 2 == 0: 
        return (m + minTiles(int(n/2), int(m/2))) 
  
    # If n and m are odd, add row + column number of tiles 
    else: 
        return (n + m - 1 + minTiles(int(n/2), int(m/2)))

print(minTiles(8,10))







'''
------------------------------------------------------------------------------
Back Track Sudoku
'''


board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -  ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")

print_board(board)



def solve(bo):
    find = find_empty(bo)#tìm vị trí ô trống đầu tiên
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(bo, i, [row, col]):#tìm xem hàng có số i ko
            bo[row][col] = i #nếu true gán giá trị

            if solve(bo):#đệ quy
                return True

            bo[row][col] = 0#nếu ko làm đc thì làm lại bước trước
    return False

def valid(bo, num, pos):
    # Check row
    for i in range(9):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(9):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and [i,j] != pos:
                return False

    return True


def find_empty(bo):
    for row in range(len(bo)):
        for col in range(len(bo[0])):
            if bo[row][col] == 0:
                return row, col 

    return None

print_board(board)
solve(board)
print("_______________________")
print_board(board)