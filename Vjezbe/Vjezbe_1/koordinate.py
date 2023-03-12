while True:
    x1 = input('x1: ')
    y1 = input('y1: ')
    x2 = input('x2: ')
    y2 = input('y2: ')
    try:
        float(x1) and float(y1) and float (x2) and float(y2)
        break
    except ValueError:
        print('Ponovo.')

x1 = float(x1)
y1 = float(y1)
x2 = float(x2)
y2 = float(y2)

k = (y2-y1)/(x2-x1)
l = y1-k*x1

if k==1.0:
    if l>0:
        print('y=x+{}'.format(l))
    elif l<0:
        print('y=x{}'.format(l))
    else:
        print('y=x')

elif k==-1.0:
    if l>0:
        print('y=-x+{}'.format(l))
    elif l<0:
        print('y=-x{}'.format(l))
    else:
        print('y=-x')

elif k==0.0:
    print('y={}'.format(l))
    
else:
    if l>0:
        print('y={}x+{}'.format(k,l))
    elif l<0:
        print('y={}x{}'.format(k,l))
    else:
        print('y={}x'.format(k))

