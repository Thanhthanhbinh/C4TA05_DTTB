'''
                                            |LIST|                                           
---------------|THEORY|----------------
NOTE:
index: starts from 0 to n
[-1]==[n]
NOTE:
loop: for i in list --print(value)
loop: for i in range (len(list)) --print(index)
loop: for i,j in enumerate(list)--print(index,value)
NOTE:
update:
    list[n]=a
    list[1],list[2]=list[2],list[1]--switch positions
NOTE:
delete: del list[1]
NOTE:
list slicing: 
a=[1,2,3,4,5]
a[:]--all value in a-[1,2,3,4,5]
a[:2]--take value from start to a[1]-[1,2]
a[3:4]--take value from a[2] to a[3]-[3,4]
a[-2:]--take value from a[-2] to end-[4,5]

'''
#---------------------BAI1---------------------
#random list 10 so
from random import randint
ten_list=[]
for i in range(10):
    ten_list.append(randint(1,10))
print(ten_list)
'''
#new list three first values
three_list=[]
for i in range(3):
    three_list.append(ten_list[i])
print(three_list)
print(ten_list[ :3])
#new list last three value
rev_three_list=[]
for i in range(len(ten_list)-1,len(ten_list)-4,-1):
    rev_three_list.append(ten_list[i])
print(rev_three_list)
print(ten_list[-3: ])
'''
'''
USE LIST SLICING | FOR THE ABOVE
'''
#rearrange list max to min
loop=True
counter=0
while loop:
    for i in range(len(ten_list)-1):
        if ten_list[i]<ten_list[i+1]:
            ten_list[i],ten_list[i+1]=ten_list[i+1],ten_list[i]
            counter+=1
    if counter==0:
        loop=False
    else:
        counter=0
    print(ten_list)





