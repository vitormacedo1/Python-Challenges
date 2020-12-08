import urllib
import urllib.request

try:
    site = urllib.request.urlopen('HTTP://www.pudim.com.br')
except urllib.error.URLError:
    print('Site não acessivel no momento')
else:
    print('Site acessado com sucesso.')
    