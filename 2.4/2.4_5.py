c = 0
s = ''
for i in range(int(input())):
    a = input()
    while a != 'ВСЁ':
        s = s + a + ' '
        a = input()
    if 'зайка' in s:
        c += 1
    s = ''
print(c)