'''
______________________|BACKTRACK|________________________
'''
bo=[
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0]
]
def print_solution(broad):
    for i in range(5):
        for j in range(5):
            print(broad[i][j],end=' ')
        print()
def solve(bo,pos,number):
    if number>25:
        return True
    row=pos[0]
    col=pos[1]
    move_x=[2,1,-1,-2,-2,-1,1,2]
    move_y=[1,2,2,1,-1,-2,-2,-1]
    #move in "l" suitable?
    for j in range(len(move_x)):
        new_x=row+move_x[j]
        new_y=col+move_y[j]
        if valid(bo, number, [new_x, new_y]):#tìm xem "above"
            bo[new_x][new_y] = number #nếu true gán giá trị
            if solve(bo,[new_x,new_y],number+1)==True:#đệ quy
                return True
            bo[new_x][new_y] = 0#nếu ko làm đc thì làm lại bước trước
    return False
#___|ABOVE|___
# đi chữ l
# ko đi vào chỗ đã đi
# khác số
# inside broad
def valid(bo,i,pos):
    #within the broad
    if (pos[0] < len(bo) and pos[1] < len(bo[0]) and pos[0]>=0 and pos[1]>=0 and bo[pos[0]][pos[1]]==0):
        return True
    return False
    

def find_empty(bo):
    for row in range(len(bo)):
        for col in range(len(bo[0])):
            if bo[row][col] == 0:
                return True 

    return False
bo[0][0]=1
print(solve(bo,[0,0],2)   )
print_solution(bo)


