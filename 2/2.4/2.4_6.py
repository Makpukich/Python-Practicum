b = 0
for i in range(int(input())):
    a = int(input())
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    b = b + a
print(b)