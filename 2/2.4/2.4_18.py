a = int(input())
s = ''
b = a
c = 0
while b > 0:
    c += 1
    b -= c
n = 1
arr = []
for i in range(c):
    for j in range(i + 1):
        if n > a:
            break
        s = s + str(n) + ' '
        n += 1
    arr.append(s)
    s = ''
maxlen = len(arr[-1])
for i in range(c):
    arr[i] = f'{arr[i]:^{maxlen}}'
for i in arr:
    print(i)