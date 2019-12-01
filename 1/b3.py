#check snt
inp=int(input("enter number:"))
k=0
for i in range(1,inp):
    if inp%i==0:
        k+=1
if k==1:
    print("yes")
else:
    print("no")
