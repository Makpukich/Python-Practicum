a = input()
x = 0
y = 0

while a != 'СТОП':

    b = int(input())

    if a == 'СЕВЕР':
        y += b
    if a == 'ВОСТОК':
        x += b
    if a == "ЮГ":
        y -= b
    if a == 'ЗАПАД':
        x -= b

    a = input()

print(y)
print(x)