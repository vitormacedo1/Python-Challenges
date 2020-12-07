from datetime import date
trabalho = {}
idade = {}
trabalho['Nome'] = str(input('Nome: ')).strip().capitalize()
idade['Ano de nascimento'] = int(input('Ano de nascimento: '))
ridade = date.today().year - idade['Ano de nascimento']
trabalho['Idade'] = ridade
trabalho['Carteira de trabalho'] = int(input('Nº da carteira de trabalho:[0 se não tiver] '))
if trabalho['Carteira de trabalho'] != 0:
    idade['Ano de contratação'] = int(input('Ano de contratação: '))
    trabalho['Aposentadoria'] = date.today().year - idade['Ano de contratação'] + 35 + ridade
    trabalho['Salário'] = int(input('Salário: '))

print('-=' * 23)
for k, l in trabalho.items():
    print(f'{k} corresponde a {l}')
    