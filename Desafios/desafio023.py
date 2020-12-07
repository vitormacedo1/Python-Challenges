n = int(input('Informe um numero: '))
ns = str(n)
u = d = c = m = 0
if n <= 9:
    u = ns[0]
elif 9 < n < 100:
    d = ns[0]
    u = ns[1]
elif 100 <= n <= 999:
    c = ns[0]
    d = ns[1]
    u = ns[2]
elif n >= 1000:
    m = ns[0]
    c = ns[1]
    d = ns[2]
    u = ns[3]
print(f'Unidades: {u}\n'
      f'Dezenas: {d}\n'
      f'Centenas: {c}\n'
      f'Milhas: {m}')
