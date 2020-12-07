from datetime import date


def voto(v):
    """
        -> v analyzes if the values of
        'idade' are 18 or more and less than 65
        for 'VOTO OBRIGATÓRIO', in Between 16 and 18
        for 'VOTO OPTATIVO' and less than 16 for 'NÃO VOTA'

    """
    if 18 <= v < 65 :
        return 'VOTO OBRIGATÓRIO'
    elif 16 <= v < 18 or v >= 65:
        return 'VOTO OPTATIVO'
    else:
        return 'NÃO VOTA'



ano = int(input('Ano de nascimento: '))
idade = date.today().year - ano
vot = voto(idade)
print(f'Com {idade} anos: {vot}')
