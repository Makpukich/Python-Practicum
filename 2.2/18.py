a = int(input())
b = int(input())
c = int(input())
lst = [a, b, c]
lst.sort()
hu = lst[0] ** 2 + lst[1] ** 2
if hu > lst[2] ** 2:
    print("крайне мала")
elif hu == lst[2] ** 2:
    print("100%")
else:
    print('велика')