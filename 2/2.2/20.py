a = input()
b = input()
c = input()
lst = []
if "зайка" in a:
    lst.append(a)
if "зайка" in b:
    lst.append(b)
if "зайка" in c:
    lst.append(c)
lst.sort()
print(lst[0], len(lst[0]))