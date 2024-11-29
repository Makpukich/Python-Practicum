def v(n):
    a, b, c = 0, 0, 0
    for i in range(1, n):
        for j in range(1, n):
            for t in range(1, n):
                if i + j + t == n:
                    print(i, j, t)


print('А Б В')
n = int(input())
v(n)