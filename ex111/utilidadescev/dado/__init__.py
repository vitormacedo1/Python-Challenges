def leiaDinheiro(n):
    pas = False
    while not pas:
        entrada = str(input(n)).replace(',', '.').strip()
        if entrada.isalpha() or entrada.strip() == '':
            print(f'ERROR: \"{entrada}\" é um preço inválido')
        else:
            pas = True
            return float(entrada)