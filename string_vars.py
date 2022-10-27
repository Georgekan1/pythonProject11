s='abcdefghf'
print(s)
print(len(s))
print(s.count('f'))
s.__doc__
print(s.find('fc'))
print(s[2:5])
print(s[2:])
#first 2 characters
print(s[:2])
#last 2 characters
print(s[-2:])



print('--------')
s2= 'abc\ndef\tfagagaφςεγφεργ\tgwrgw'
print(s2)

print(ord('a'))
print(ord('A'))


s3 = '       asfef   regtet  '
#getting rid of spaces front and back
print(s3.strip())

s4= '77'
s5 = '43563.5436'
i4 = int(s4)
f5 = float(s5)
c = i4 + f5
print(type(c))
print(c)

s8 = 'absferereg;fregerge;53453;2356254;54'
print(s8.split(';'))
print(s8.split(';')[2])





