#NOTE:10 MAY 2020|||||||AFTER CORONA/COVID-19
#----------------------ANSWER OF MID_TERM----------------------
#Question 1
def sum_of_digit(n):
    if n==0:
        return 0
    return n%10 + sum_of_digit(int(n/10)) # OR USE 'n//10' INSTEAD
#Question 2
def sum_first_numbers(n):
    if n==0:
        return 0
    return n+sum_first_numbers(n-1)
#Question 5
def isReachable (sx,sy, dx,dy):
    if (sx>dx or sy >dy):
        return False
    if (sx==dx and sy==dy):
        return True
    return (isReachable(sx+sy, sy, dx,dy)) or (isReachable(sx,sy+sx,dx,dy))
#Question 6 IT'S A PATTERN THAT YOU MUST FIND
def reachTarget (target):
    target=abs(target)#ABSOLUTE VALUKE
    sum=0
    step=0
    while (sum<target or (sum-target)% 2!=0):
        step=step+1
        sum=sum+step
    return step