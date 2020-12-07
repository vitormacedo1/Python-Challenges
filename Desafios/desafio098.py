from time import sleep


def contagem(a, b, c):
    print('-=' * 17)
    if c == 0:
        c = 1
    print(f'Contagem de {a} até {b} de {abs(c)} em {abs(c)}')
    if a < b:
        for q in range(a, b + c, abs(c)):
            print(f'{q}  ', end='')
            
            sleep(0.5)
        print()
    elif a > b: 
        if c > 0:
            for q in range(a, b - c, c * -1):
                print(f'{q}  ', end='')
                sleep(0.5)
            print()
        elif c < 0:
            for q in range(a, b + c, c):
                print(f'{q}  ', end='')
                sleep(0.5)
            print()
    

### MAIN PROGRAM ###

contagem(1, 10, 1)
contagem(10, 0, 2)
print('-=' * 17)
print('Agora é sua vez de personalizar a contagem!')
a = int(input('Início: '))
b = int(input('Final: '))
c = int(input('Passo: ')) 
contagem(a, b, c)
print('FIM!')
print('-=' * 17)
