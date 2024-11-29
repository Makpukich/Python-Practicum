a = int(input())
summ = 0
for i in range(a):
    summ += sum(list(map(int, list(input()))))
print(summ)