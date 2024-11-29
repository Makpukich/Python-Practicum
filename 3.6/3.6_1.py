for _ in range(int(input())):
    a = input()
    A, B, S = a.split('&')
    A = int(A)
    B = int(B)
    r = ''
    for i in range(A, len(S), 2):
        r += S[i]
        if len(r) == B:
            break
    print(r)
