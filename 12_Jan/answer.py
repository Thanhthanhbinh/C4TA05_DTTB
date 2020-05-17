#Question 1
'''
def sum_number(num):
    num_sum=0
    for i in range(len(num)):
        a=int(num[i])
        num_sum+=a
    return num_sum
print(sum_number('1234'))
'''
#Question 2
'''
def sum_number(n):
    if n==0:
        return 0
    elif n==1:
        sum_n=1
        return sum_n
    else:
        sum_n=n+sum_number(n-1)
    return sum_n
print(sum_number(4))
'''
#Question 3
#-------------FIND MAX NUMBER IN LIST----------------
'''
def find_num(num_list):
    max_num=num_list[0]
    if len(num_list)<=1:
        return max_num
    else:
        if max_num<find_num(num_list[1:]):
            max_num=find_num(num_list[1:])
    return max_num    
print(find_num([3,2,4,2,1,44,2,3,2,23]))
'''
#--------FIND SUM OF LIST'S ELEMENTS-------------
'''
def sum_list(num_list):
    sum_num=num_list[0]
    if len(num_list)<=1:
        return sum_num
    else:
        sum_num+=sum_list(num_list[1:])
    return sum_num
print(sum_list([1,2,3,4]))
'''
#--------------REVERSE GIVEN LIST---------------
'''
def reverse_list(num_list):
    num=[num_list[len(num_list)-1]]
    if len(num_list)<=1:
        return num
    else:
        new_list=num_list
        new_list.pop(len(new_list)-1)
        for i in reverse_list(new_list):
            num.append(i)
    return num
print(reverse_list([1,2,3,4]))
'''
#Question 4
#-----------SOLVE MAZE----------------
'''
def maze_solve(maze,pos):
    if pos==[len(maze)-1,len(maze)-1]:
        return True
    add_x=[1,0]
    add_y=[0,1]
    for i in range(len(add_x)):
        new_x=pos[0]+add_x[i]
        new_y=pos[1]+add_y[i]
        if valid(maze,new_x,new_y):
            new_pos=[new_x,new_y]
            maze[new_x][new_y]=2
            if maze_solve(maze,new_pos)==True:
                return True
            maze[new_x][new_y]=1
    return False
def valid(maze,new_x,new_y):
    if (new_x<len(maze) and new_y<len(maze) and maze[new_x][new_y]==1):
        return True
    return False


maze = [[2, 0, 0, 0], 
        [1, 1, 0, 1], 
        [0, 1, 1, 0], 
        [1, 0, 1, 1]]
print(maze_solve(maze,[0,0]))
print(maze)
'''
#Question 5 
#NOTE 10 MAY: check this again this might be wrong, suing de quy
'''
bc co 2 th: True and False
true-end, false-back
if false again the use new destination as the loop
there is a limit of moving, a certain area
'''
def point_move(pos,end,avoid):
    if pos==end:
        return True
    add_x=[pos[1],0]
    add_y=[0,pos[0]]
    for i in range(len(add_x)):
        new_x=pos[0]+add_x[i]
        new_y=pos[1]+add_y[i]
        if valid(new_x,new_y,avoid):
            if point_move([new_x,new_y],end,avoid)==True:
                return True
            avoid.append([new_x,new_y])
    return False
def valid(new_x,new_y,avoid):
    if [new_x,new_y] not in avoid:
        return True
    return False
print(point_move([1, 2,],[ 3, 4],avoid))
#Question 6
#//////////////////////CHECK ANS.PY FOR THE TRUE ANSWER\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
