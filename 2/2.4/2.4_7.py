a = int(input())
for i in range(1, a + 1):
    for j in range(2 + i, 0, -1):
        print(f'До старта {j} секунд(ы)')
    print(f'Старт {i}!!!')