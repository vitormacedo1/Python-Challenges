nome = str(input('Digite uma frase: ')).lower().strip()
print('A letra A aparece {} vezes.'.format(nome.count('a')))
print('A primeira letra A aparece na {} posição'.format(nome.find('a')+1))
print('A ultima letra A aparece na {} posição'.format(nome.rfind('a')+1))