
seq = (int(input('Digite um valor: ')), int(input('Digite um valor: ')),
       int(input('Digite um valor: ')), int(input('Digite um valor: ')), )
print(f'o numero 9 apareceu {seq.count(9)} vez')
if 3 in seq:
    print(f'O numero 3 apreceu na posição {seq.index(3) + 1} ')
else:
    print('A sequencia não possui o numero 3.')
print('Os numeros pares são: ', end='')
for n in seq:
    if n % 2 ==0:
        print(n)
print(f'A sequencia digitada foi: {seq}')
