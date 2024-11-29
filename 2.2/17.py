a = float(input())
b = float(input())
c = float(input())
lst = []
d = b ** 2 - 4 * a * c
if a == 0:
    if b == 0 and c == 0:
        print("Infinite solutions")
    elif b == 0:
        print("No solution")
    elif c == 0:
        print("0")
    else:
        print(f'{(-1 * c) / b:.2f}')
elif b == 0 and c == 0:
    print('0')
elif d < 0:
    print("No solution")
else:
    lst.append(f'{(-1 * b - d ** 0.5) / (2 * a):.2f}')
    lst.append(f'{(-1 * b + d ** 0.5) / (2 * a):.2f}')
    lst = set(list(map(float, lst)))
    lst = list(lst)
    lst.sort()
    print(*lst)