a = int(input())
b = int(input())
c = len(str(a * b))
n = 1


def lenfix(x, y):
    while len(x) != y:
        x = ' ' + x
    return x


for i in range(a):
    if i % 2 == 0:
        n = b * i + 1
    else:
        n = b * i + b
    for j in range(b):
        print(lenfix(str(n), c), end=' ')
        if i % 2 == 0:
            n += 1
        else:
            n -= 1
    print()
