'''
                                            |LIST|                                       
---------------|THEORY|----------------
|||||||ROOM FOR IMPROVEMENTS|||||||
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
                                            |DICTIONARY|
NOTE:
dict={
    "a":1,
    "b":2,
}
NOTE:
loop: for i in dict --print(key)-1,2
loop: for i in dict.values() --print(value)
NOTE:
update:
dict['c']=3
NOTE:
delete: del dict['a']/dict['b']/etc
NOTE:
dict['a']=dict.pop('A') --change key

'''
#---------------------BAI1---------------------
'''
#random list 10 so
from random import randint
ten_list=[]
for i in range(10):
    ten_list.append(randint(1,10))
print(ten_list)
'''
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
'''
#rearrange list max to min
loop=True
while loop:
    loop=False
    for i in range(len(ten_list)-1):
        if ten_list[i]<ten_list[i+1]:
            ten_list[i],ten_list[i+1]=ten_list[i+1],ten_list[i]
            loop=True
print(ten_list)
'''
#-----------------BAI2--------------
multi_list=[1,3,4,16,32,8,64,4,128,2,256,32]
multi_dict={}
multi_ind={}
multi_sum=[]
for j in range(len(multi_list)-1):
    first=multi_list[j]
    for i in range(len(multi_list)-1):
        if first!=multi_list[i]:
            if first*multi_list[i]==256 and first+multi_list[i] not in multi_sum:
                multi_dict[first]=multi_list[i]
                multi_ind[j]=i
                multi_sum.append(first+multi_list[i])
print(multi_dict)







