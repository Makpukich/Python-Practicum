pet = int(input())
vas = int(input())
tol = int(input())

if pet > vas > tol:
    gold = 'Петя'
    silv = "Вася"
    bron = "Толя"
elif pet > tol > vas:
    gold = 'Петя'
    silv = 'Толя'
    bron = 'Вася'
elif vas > pet > tol:
    gold = 'Вася'
    silv = 'Петя'
    bron = 'Толя'
elif vas > tol > pet:
    gold = 'Вася'
    silv = 'Толя'
    bron = 'Петя'
elif tol > pet > vas:
    gold = 'Толя'
    silv = 'Петя'
    bron = 'Вася'
elif tol > vas > pet:
    gold = 'Толя'
    silv = 'Вася'
    bron = 'Петя'
print(f'{gold.center(24, " ")}')
print(f'{(silv.center(8, ' ')).ljust(24, ' ')}')
print(f'{(bron.center(8, ' ')).rjust(24, ' ')}')
print("   II      I      III   ")