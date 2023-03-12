import matplotlib.pyplot as plt

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

def koordinate(x1,y1,x2,y2):
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

koordinate(x1,y1,x2,y2)

x = [x1,x2]
y = [y1,y2]

plt.plot(x,y)
plt.title('Graf')
plt.xlabel('x-os')
plt.ylabel('y-os')

a = input('Želite li spremiti datoteku kao PDF? (da/ne) ')

if a=='da':
    naziv=input('Upišite ime pod kojim želite da Vam se datoteka spremi: ')
    plt.title(naziv)
    plt.savefig('{}.pdf'.format(naziv))
elif a=='ne':
    plt.show()