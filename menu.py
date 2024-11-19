from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *

pygame.font.init()
custom_font = pygame.font.Font("fonts/PressStart2P-Regular.ttf", 32)

def posInicialPersonagem(sprite):
    sprite.set_position(110,470)

def obstaculoInicial(sprite):
    sprite.set_position(700,490)


janela = Window(1024,682)
background = GameImage("images/background_prisao.png")
personagem1 = Sprite("images/deolene.png")
personagem2 = Sprite("images/guilherme.png")
carrinhoLimpeza = Sprite("images/carrinholimpeza.png")
policial = Sprite("images/policial.png")
moeda = Sprite("images/coin.png")
janela.set_title("FASE 1: PRISÃO")
moedas = 0

#posInicialPersonagem(personagem1)
posInicialPersonagem(personagem2)
while True:
    #posicioes Iniciais:
    obstaculoInicial(policial)
    #obstaculoInicial(carrinhoLimpeza)
    personagem1.move_key_y(0.5)
    moeda.set_position(55,35)

    background.draw()
    
    #personagem1.draw()
    #carrinhoLimpeza.draw()
    personagem2.draw()
    policial.draw()
    texto = custom_font.render(str(moedas), True, (255,251,100))
    janela.screen.blit(texto, (130, 50)) 
    moeda.draw()

    janela.update()