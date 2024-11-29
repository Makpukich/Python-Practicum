a = int(input())
b = 1
c = 1
for i in range(a):
    for i in range(b):
        print(c, end=' ')
        c += 1
        if c > a:
            quit()
    print()
    b += 1