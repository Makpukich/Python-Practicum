start = int(input())
end = int(input())
a = (-1 * (start > end) + 1 * (start < end) + 0)
while start != end:
    print(start, end=' ')
    start += a
print(end)
