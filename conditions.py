p = True
q = False

if p:
    print(' p is True')
else:

    print('p is False')

if p and q:
    print('p and q is True')
else:
    print('p and q are False')
if p or q:
    print('p or q is True')
else:
    print('p or q are False')

if p ^ q:
        print('p xor q is True')
else:
        print('p xor q are False')

if p and not q:
        print('p and not q is True')
else:
        print('p and not q are False')

v = None

#if v:
       # print('v={}'.format(v))
#else:
        #print('not v')

#errors for both string and int and other types
#t = '55'
#tt = t + v
#print(tt)

#this will work
#v = ''
#t = '55'
#tt = t + v
#print(tt)


w = 13
z = 8.8

if w> z:
    print('w > z')
else:
    print('w not > z')

w = 13
z = 8.8

a=43



if w>= z:
    print('w >= z')
else:
    print('w not >= z')

w = 'abce'
z = 'abc'

if w== z:
    print('w == z')
else:
    print('w not == z')


y = 10  if w=='abce'  else 20
print(f'y={y}')
print('y={}'.format(y))
#print('y=' + str(y))