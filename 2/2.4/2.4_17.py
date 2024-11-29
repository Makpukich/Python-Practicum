c = 0
for i in range(int(input())):
    a = input()
    if a == a[::-1]:
        c += 1
print(c)
