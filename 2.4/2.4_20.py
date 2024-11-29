def f(x, y):
    b = ''
    while x > 0:
        b = str(x % y) + b
        x = x // y
    return b


a = int(input())
ms = 0
mc = 11
for i in range(2, 11):
    if sum(list(map(int, list(f(a, i))))) > ms:
        ms = sum(list(map(int, list(f(a, i)))))
        mc = i
print(mc)