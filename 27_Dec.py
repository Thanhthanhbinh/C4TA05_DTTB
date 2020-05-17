#limit line
#height=2n+1
'''
đặt tên
độ dài
    file
    hàm
    dòng_word limit
hàm
biến toàn cục

tách file: chỉ liên quan đến tính toán, ui, 
tra coding convention
'''
height=7
line=[]
for i in range(height):
    line.append('')
for i in range(0,(height-1)//2+1):
    for j in range(0,(height-1)//2+1):
        if ((height-1)//2)-i==j:
            for k in range(i*2+1):
                print("*",end="")
        else:
            print(".",end="")
    print('\n')
for i in range(0,(height-1)//2+1):
    for j in range(0,(height-1)//2+1):
        if ((height-1)//2)-i==j:
            for k in range(i*2+1):
                print("*",end="")
        else:
            print(".",end="")
    print('\n')
'''
 0123456
0...*...
1..***..
2.*****.
3*******
4.*****.
5..***..
6...*...

'''