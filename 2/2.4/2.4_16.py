a = int(input())
lettlen = int(input())
alen = lettlen * a + a - 1
for i in range(a):
    n = i + 1
    for j in range(a):
        if j != a - 1:
            print(f'{n * (j + 1):^{lettlen}}|', end='')
        else:
            print(f'{n * (j + 1):^{lettlen}}', end='')
    print()
    if i != a - 1:
        print('-' * alen)
