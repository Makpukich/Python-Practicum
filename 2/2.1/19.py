name = input()
cost = int(input())
weight = int(input())
money = int(input())
stri = f'{weight}кг * {cost}руб/кг'
print("Чек".center(35, "="))
print(f'Товар:{name.rjust(29, " ")}')
print(f'Цена:{stri.rjust(30, " ")}')
print(f'Итого:{str(cost * weight).rjust(26, ' ')}руб')
print(f'Внесено:{str(money).rjust(24, ' ')}руб')
print(f'Сдача:{str(money - cost * weight).rjust(26, ' ')}руб')
print('=' * 35)
