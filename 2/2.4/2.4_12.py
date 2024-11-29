a = int(input())
b = int(input())
c = len(str(a * b))
n = 1


def lenfix(x, y):
    while len(x) != y:
        x = ' ' + x
    return x


for i in range(a):
    for j in range(b):
        print(lenfix(str(n), c), end=' ')
        n += 1
    print()
