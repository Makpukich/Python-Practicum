x = float(input())
y = float(input())
inParab = False
inLine = False
inCirc = False
undLine = False
if (x ** 2 + y ** 2) <= 100:
    if y <= 0:
        if y > 0.25 * x ** 2 + 0.5 * x - 8.75:
            inParab = True
    elif y > 0 and -7 <= x <= -4:
        if y < x * 5 / 3 + 35 / 3:
            inLine = True
    elif y <= 5 and -4 < x <= 0:
        undLine = True
    elif x ** 2 + y ** 2 <= 25:
        inCirc = True
    if inParab + inLine + undLine + inCirc == 1:
        print('Опасность! Покиньте зону как можно скорее!')
    else:
        print('Зона безопасна. Продолжайте работу.')
else:
    print('Вы вышли в море и рискуете быть съеденным акулой!')
