
'''
for i in range (0,29,2):
    print(i)
for i in range (28,0,-2):
    print(i)
'''

'''
inp=int(input("enter: "))
inp=str(inp)
count=0
for i in inp:
    try:
        i=int(i)
    except:
        count+=1
print(len(inp)-count)
'''

loop=True
up_b=100
under=0
while loop:
    print((up_b+under)//2)
    print('''
    c:correct
    l:larger
    s:smaller ''')
    inp=str(input("enter:"))
    if inp=="c":
        loop=False
    elif inp=="l":
        under=(up_b+under)//2
    elif inp=='s':
        up_b=(up_b+under)//2
'''
loop=True
inp=int(input("number: "))
count=0
while loop:
    if (inp//10)>0:
        count+=1
        inp=inp//10
    else:
        loop=False
print(count+1)        
'''