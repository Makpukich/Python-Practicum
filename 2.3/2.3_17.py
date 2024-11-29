a = input()
c = list(a)
for i in range(len(c)):
    if c[i] in ['0', '2', '4', '6', '8']:
        c[i] = ''
print(''.join(c))