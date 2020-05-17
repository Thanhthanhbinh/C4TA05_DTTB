'''_________________________|BAI TAP DE QUY FROM SESSION 3 IN 8_DEC|____________________________'''
#------------------------------function find minimun value---------------------------
#_______|NORMAL|________
'''
def find_minimum(l):
    min_result=l[0]
    for i in l:
        if min_result>i:
            min_result=i
    return min_result
'''
#_______|ADVANCE|________
'''
def find_minimum(l):
    min_result=l[0]
    if len(l)==1:
        return min_result
    else:
        del l[0]#slice list instead l[1:]
        if min_result>find_minimum(l):
            min_result=find_minimum(l)
        return min_result
print(find_minimum([32,23,4,4,2,3,1,31]))
'''
#-----------------------function find the greates common divison--------------------
#_________|NORMAL|__________
'''
def greatest_divison(a,b):
    if a%b==0:
        return b
    elif b%a==0:
        return a
    else:
        if a<b:
            for i in range (1,a):
                if a%i==0 and b%i==0:
                    result=i
            return result
        else:
            for i in range (1,b):
                if a%i==0 and b%i==0:
                    result=i
            return result
'''
#_________|ADVANCE|__________
'''
def greatest_divison(a,b):
    if a==b:
        return a
    else:
        if a>b:
            b=a-b
            a=b
            result=greatest_divison(a,b)
            return result
        else:
            a=b-a
            b=a
            result= greatest_divison(a,b)
            return result
print(greatest_divison(12,18))
'''
#----------------------------function candy, money, wrap-----------------------------
#_________|NORMAL|__________
'''
def candy(mon,pri,war):
    candy=mon//pri
    loop=True
    warp=candy
    can=0
    while loop:
        lwarp=warp%war
        warp=warp//war
        can+=warp
        warp+=lwarp
        if warp<war:
            loop=False
        
    return candy+can
'''
#_________|ADVANCE|__________
'''
def candy1(mon, pri,war):
    cand=mon//pri
    return cand+candy(war,cand)

def candy(war,candy1):
    warp=candy1
    lwarp=warp%war
    warp=warp//war
    can=warp
    warp+=lwarp
    if warp<war:
        return can
    else:
        result=can+candy(war,warp)
        return result

print(candy1(16,2,2))
'''
#--------------------------function binary number---------------------------
#_________|NORMAL|__________
'''
def binary(a):
    num=a
    loop=True
    no=""
    while loop:
        no+=str(num%2)
        num=num//2
        if num==0:
            loop=False
    return no[::-1]
'''
#_________|ADVANCE|__________
'''
def binary(a):
    num=a
    if num==0:
        no=0
        return no
    else:
        no=num%2+10*binary(num//2)
        return no
print(binary(450))
'''
#--------------------------function substring--------------------------
#_________|ADVANCE|__________
'''
def substringf(a):
    if len(a)==0:
        return 0
    else:
        valid=substringf(a[1:])+substringf(a[:-1])-substringf(a[1:-1])
        if a[0]==a[-1]:
            valid+=1
        return valid
print(substringf('abcabcab'))
'''
#--------------------------function pascal triangle--------------------------
def pascal(number):
    loop=True
    ori_list=[1,1]
    counter=0
    while loop:
        a=ori_list
        for i in range(len(ori_list)):
            a.insert(i+1,ori_list[i]+ori_list[i+1])
        counter+=1
        ori_list=a
        if counter==number:
            loop=False
            return ori_list
print(pascal(2))

