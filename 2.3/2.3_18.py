a = int(input())
lst = []
while a > 1:
    for i in range(2, a + 1):
        if a % i == 0:
            lst.append(i)
            a = a // i
            break

print(' * '.join(map(str, lst)))