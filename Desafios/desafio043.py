import pygame
print('Descubra com está seu IMC e se seu peso está bom!')
peso = float(input('Digite seu Peso(em KG): '))
altura = float(input('Digite sua Altura: '))
imc = peso / altura ** 2
if imc <= 18.5:
    print('Tem que comer mais feijão.')
elif 18.5 < imc <= 25:
    print('Ta com o peso TOP!')
elif 25 < imc <= 30:
    print('Ta meio gordinho, vai caminhar.')
elif 30 < imc < 40:
    print('Tu ta com obesidade meu chapa.')
else:
    pygame.mixer.init()
    pygame.init()
    pygame.mixer.music.load('baleia.mp3')
    pygame.mixer.music.play()
    pygame.event.wait()
    while pygame.mixer.music.get_busy(): pass
    print('Eu acho que você já entendeu...')
print('Seu IMC é de {:.2f}'.format(imc))
