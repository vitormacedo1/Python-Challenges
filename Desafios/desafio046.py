import  pygame
from time import sleep
start = int(input('DIGITE " 1 " PARA COMEÇAR OS FOGOS: '))

if start == 1:
    for c in range(10, -1, -1):
        print(c)
        sleep(1)
    print('FELIZ ANO NOVO!')
    pygame.mixer.init()
    pygame.init()
    pygame.mixer.music.load('fogos_de_artificio.mp3')
    pygame.mixer.music.play()
    pygame.event.wait()
    while pygame.mixer.music.get_busy(): pass


else:
    print('Numero inválido. Tente novamente.')

