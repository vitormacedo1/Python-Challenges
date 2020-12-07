c = input('Digite o nome da sua cidade: ')
qw = c.lower().title()
r = 'Santo' in qw
print(qw)
if not r:
    print('A cidade {} NÃO possui Santo no nome.'.format(c))
if r:
    print('A cidade {} TEM Santo no nome.'.format(c))
