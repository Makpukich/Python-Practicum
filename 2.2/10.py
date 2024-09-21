a = input()
num1 = 0
num2 = 0
num1 = int(a[0]) + int(a[1])
num2 = int(a[1]) + int(a[2])
if num1 > num2:
    print(f'{num1}{num2}')
else:
    print(f'{num2}{num1}')
