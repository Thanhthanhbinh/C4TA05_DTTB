#try and except
loop=True
while loop:
    inp=input('enter: ')
    try:
        inp=float(inp)
        inp=int(inp)
        loop=False
    except ValueError:
        print('Wrong')
    







