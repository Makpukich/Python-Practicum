hours = int(input())
mins = int(input())
time = int(input())
time = time + hours * 60 + mins
time = time % (24 * 60)
print(f'{time // 60:02}:{time % 60:02}')