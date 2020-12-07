import pygame
pla = str(input('Digite play para começar a musica: ')).upper()
st = str(input('Digite stop para pausar a musica: ')).upper()
if pla == 'PLAY':
    pygame.mixer.init()
    pygame.init()
    pygame.mixer.music.load('ex021.mp3')
    pygame.mixer.music.play()
    pygame.event.wait()
    while (pygame.mixer.music.get_busy()): pass
if st == 'STOP':
    pygame.mixer.music.pause('ex021.mp3')




