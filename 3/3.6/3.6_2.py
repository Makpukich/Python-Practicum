a = input()
dik = {}
while a != '':
    b = a.split()
    for i in b:
        if i[-1].upper() not in dik.keys():
            dik.update({i[-1].upper(): [i.lower()]})
        elif i.lower() not in list(dik.get(i[-1].upper())):
            dik.update({i[-1].upper(): list(dik.get(i[-1].upper())) + [i.lower()]})
        else:
            continue
    a = input()
for i in list(dik.keys()):
    print(f'{i} - ', end='')
    for j in range(len(list(dik.get(i)))):
        c = list(dik.get(i))
        c.sort()
        if j == 0:
            print(f'{c[j]}', end='')
        else:
            print(f', {c[j]}', end='')
    print()
