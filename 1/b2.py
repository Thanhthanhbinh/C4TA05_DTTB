#check nam nhuan
inp=int(input("enter year:"))
if inp%4==0 :
    print("Yes, {} is a leap year.".format(inp))
else:
    print("no, {} is not a leap year.".format(inp))