a = input()
c = 0
while a != "Приехали!":
    if 'зайка' in a:
        c += 1
    a = input()
print(c)
