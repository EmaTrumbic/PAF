while True:
    x1 = input('x1: ')
    y1 = input('y1: ')
    x2 = input('x2: ')
    y2 = input('y2: ')

    if x1 != x2:
        try:
            float(x1) and float(y1) and float (x2) and float(y2)
            x1 = float(x1)
            y1 = float(y1)
            x2 = float(x2)
            y2 = float(y2)
            break
        except ValueError:
            print('Ponovo.')
    else:
        print('Ponovo.')


k = (y2-y1)/(x2-x1)
k0 = ((k*1000)//10)/100
l = y1-k*x1
l0 = ((l*1000)//10)/100

if k0==1.0:
    str1='y=x'
elif k0==-1.0:
    str1='y=-x'
elif k0==0.0:
    str1='y='
else:
    str1='y={}x'.format(k0)

if l0>0:
    str2='+{}'.format(l0)
elif l0<0:
    str2='{}'.format(l0)
else:
    str2=''

if k0==0 and l0==0:
    print('y=0.0')
else:
    print(str1+str2)