p = 0
c = 0
for i in range(int(input())):
    b = int(input())
    m = b // (256 ** 2)
    r = (b // 256) % 256
    h = (37 * (m + r + p)) % 256
    if ((b % 256) == h) and (100 >= h):
        pass
    else:
        print(i)
        quit()
    p = h
if c == 0:
    print(-1)
