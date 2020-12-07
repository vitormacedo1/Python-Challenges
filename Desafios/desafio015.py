rent = int(input('Por quantos dias o carro foi ser alugado? '))
km = float(input('Quantos KM foram rodados? '))
print(f'O valor a ser pago é {(rent * 60) + (km * 0.15)}')