n = input('Digite seu nome completo: ')
nm = n.lower()
nt = nm.title()
# print(nt)
r = 'Silva' in nt
# print(r)
if r:
    print('Que lindo nome que possui SILVA')
if not r:
    print('Que pena que seu nome não tem SILVA')