lst = list(map(int, ''.join(input())))
maxx = max(lst)
lst.remove(maxx)
print((maxx + min(lst) == max(lst) * 2) * "YES" + ((not (maxx + min(lst) == max(lst) * 2)) * "NO"))
