def f(x):
    if x == 1:
        return 0
    for i in range(2, int(x ** 0.5 + 1)):
        if x % i == 0:
            return 0
    else:
        return 1


c = 0
for i in range(int(input())):
    c += f(int(input()))
print(c)