topg = 1000
undg = 1
a = (topg - undg + 1) // 2
print(a)
b = input()
while b != 'Угадал!':
    if b == 'Больше':
        undg = a + 1
        a = ((topg + undg) // 2)
    elif b == 'Меньше':
        topg = a - 1
        a = ((topg + undg) // 2)
    print(a)
    b = input()
