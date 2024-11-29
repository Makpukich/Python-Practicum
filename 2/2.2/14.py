a = input()
a = list(map(int, ''.join(a)))
a.sort()
if a[1] == 0:
    print(f'{a[2]}{a[1]}', end=' ')
elif a[0] == 0:
    print(f'{a[1]}{a[0]}', end=' ')
else:
    print(f'{a[0]}{a[1]}', end=' ')
print(f'{a[2]}{a[1]}')
