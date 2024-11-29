a = int(input())
b = int(input())
c = len(str(a * b))


def lenfix(x, y):
    while len(x) != y:
        x = ' ' + x
    return x


for i in range(a):
    n = i + 1
    for j in range(b):
        print(lenfix(str(n), c), end=' ')
        n += a
    print()