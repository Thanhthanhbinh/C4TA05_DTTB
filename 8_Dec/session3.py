'''
-----------------------------|THEORY|------------------------------
>>>|RANDOM NEW THINGS|
NOTE:
>|POWER FUNCTION|
pow(a,b)--a:*base--b:*power number
>>>|FUNCTIONS|
//EXAMPLE: SUM FUNCION
NOTE:
>|WRITE FUNCTION|
def sum(no1,no2):--def:*summon function begin--sum/func/etc:*name--(no1,no2,etc):*parameters
    sum_no=no1_no2
    return sum_no--return: return value--no "return sum_no", print shall be "None"
NOTE:
>|CALL FUNCTION|
print(sum(2,4))--print the value of 2+4==6
sum(2,3,4)--error as there are only two parameters (no1,no2)

//EXAMPLE:SORTING FUNCTION-->CODE FROM SESSION2 IN 1_DEC
>|WRITE FUNCTION|
def sort_mami(list):
    loop=True
    while loop:
        loop=False
        for i in range(len(list)-1):
            if list[i]<list[i+1]:
                list[i],list[i+1]=list[i+1],list[i]
                loop=True
NOTE:
>|CALL FUNCTION|
list=[]
sort_mami(list)
print(list)

'''
#-----------EXERCISE--------------
#FUNCTION FIND ROOTS OF Ax^2+Bx+C
import math  
'''
def delta(a,c,b):
    no=b**2-4*a*c
    return no
def quardo(a,b,c):
    if delta(a,b,c)<0:
        return 'VO NGHIEM'
    else:
        root1=((-b+math.sqrt(delta(a,b,c)))/2*a)
        root2=((-b-math.sqrt(delta(a,b,c)))/2*a)
        if root1!=root2:
            return root1,root2
        else:
            return root2
a=int(input('a: '))
b=int(input('b: '))
c=int(input('c: '))
print(quardo(a,b,c))
'''
#FUNCTION FIND SLOPE FROM TWO COORDINANCES
'''
def slope(point1,point2):
    try:
        gradient=((point1[1]-point2[1])/(point1[0]-point2[0]))
        return gradient
    except ZeroDivisionError:
        return "dng thang vuong goc voi truc hoanh"

point1=[0,0]
point2=[0,0]
point1[0]=int(input('x1:'))
point1[1]=int(input('y1:'))
point2[0]=int(input('x2:'))
point2[1]=int(input('y2:'))
print(point1,point2)
print("dng thang co he so goc la: ",slope(point2,point1))
'''
'''
-------------------------|THEORY II|--------------------------
>>>|RECURSIVE|
def hanoi_tower_recursion(n):
    if n==1:
        result=1
    else:
        result=2*(hanoi_tower_recursion(n-1))+1
    return result
>|HÀM ĐỆ QUY|__HÀM GỌI LẠI CHÍNH NÓ TRONG LÚC NÓ CHẠY
//EXAMPLE: n=4
result=2*(hanoi_tower_recursion(3))+1
            |->=2*(hanoi_tower_recursion(2))+1
                    |-> = 2*(hanoi_tower_recursion(1))+1
                                |->2+1+1=3
=>15
//|ANOTHER WAY|
def hanoi_tower_pow(n):
    result=pow(2,n)-1
    return result
'''
#FUNCTION FACTORIAL
'''
def factorial(n):
    if n==1:
        return 1
    else:
        result=factorial(n-1)*n
    return result
print(factorial(4))
'''
#FUNCTION FIBONACI
def fibonaci(n):
    '''
    a=1
    b=1
    for i in range(n):
        c=a+b
        print(c)
        a=b
        b=c
    '''
    if n==1 or n==0:
        return 1
    else:
        result=fibonaci(n-1)+fibonaci(n-2)
        return result

print(fibonaci(5))