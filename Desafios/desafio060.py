n = int(input('Digite um numero: '))
f = 1
for c in range(n, 0, -1):
    print(c, end='')
    if c > 1:
        print(' x ', end='')
    else:
        print(' = ', end='s')
    f *= c
print(f)