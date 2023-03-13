def koordinate(x1,y1,x2,y2):
    k = (y2-y1)/(x2-x1)
    l = y1-k*x1

    if k==1.0:
        str1='y=x'
    elif k==-1.0:
        str1='y=-x'
    elif k==0.0:
        str1='y='
    else:
        str1='y={}x'.format(k)

    if l>0:
        str2='+{}'.format(l)
    elif l<0:
        str2='{}'.format(l)
    else:
        str2=''

    if k==0 and l==0:
        print('y=0.0')
    else:
        print(str1+str2)

koordinate(5,-4,7,4)