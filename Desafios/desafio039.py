from datetime import date
print('Programa para ver se já deve ou se passou a hora de se alistar')
idade = int(input('Digite o ano que nasceu: '))
ano = date.today().year
ali = ano - idade
if ali == 18:
    print('O Senhor está com 18 anos hora de se alistar!')
elif ali > 18:
    print('O Senhor está com {} anos, já deveria ter se alistado!'.format(ali))
    print('O senhor deveria ter se alistado à {} ano(s).'.format(ali - 18))
    print('Deveria ter se alistado no ano de {}'.format(ano - (ali - 18)))
else:
    print('Ainda não é sua hora jovem Padawan')
    print('Falta-lhe {} anos'.format(18 - ali))
    print('Você devera se alistar no ano de {}'.format((18 - ali) + ano))