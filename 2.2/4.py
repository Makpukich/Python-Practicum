pet = int(input())
vas = int(input())
tol = int(input())
if pet > vas > tol:
    print("1. Петя\n2. Вася\n3. Толя")
elif pet > tol > vas:
    print("1. Петя\n2. Толя\n3. Вася")
elif vas > pet > tol:
    print("1. Вася\n2. Петя\n3. Толя")
elif vas > tol > pet:
    print("1. Вася\n2. Толя\n3. Петя")
elif tol > pet > vas:
    print("1. Толя\n2. Петя\n3. Вася")
elif tol > vas > pet:
    print("1. Толя\n2. Вася\n3. Петя")