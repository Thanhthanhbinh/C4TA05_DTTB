#||||||||||||||||||||||||||\\\\WARM UP////||||||||||||||||||||||||||
#MID_TERM Question 3
#_____________FIND MAX NUMBER IN LIST_____________
'''
def max_number(list):
    max=list[0]
    if len(list)<=1:
        return max
    else:
        if max<max_number(list[1:]):
            max=max_number(list[1:])
    return max
print(max_number([3,44,1,5,4,3,21]))
'''
# list=[1,2,3,4,5]
# print(list[1:])
#_____________FIND MIN NUMBER IN LIST_____________
'''
def min_number(list):
    max=list[0]
    if len(list)<=1:
        return max
    else:
        if max>max_number(list[1:]):
            max=max_number(list[1:])
    return max
print(min_number([3,44,1,5,4,3,21]))
'''
#_____________FIND SUM NUMBER IN LIST_____________-
'''
def sum_number(list):
    n=list[0]
    if len(list)<=1:
        return n
    else:
        n=n+sum_number(list[1:])
    return n
print(sum_number([1,2,3,4]))
'''
#_____________FIND REVERSE NUMBER IN LIST_____________-
'''
def reverse_list(list):
    n=list[-1:]
    if len(list)<=1:
        return n
    else:
        for i in reverse_list(list[:-1]):
            n.append(i)
    return n
print(reverse_list([1,2,3,4]))
'''
''' CONSIDER LIST BEING EMPTY'''
#Question 6
def calculate(n):
    sum_start=0
    steps=1
    counter=0
    while sum_start<n:
        counter++
        sum_start+=counter
    