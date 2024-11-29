summ = 0
a = float(input())
while a != 0:
    if a >= 500:
        a = a * 0.9
    summ += a
    a = float(input())
print(summ)