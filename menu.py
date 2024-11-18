from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *

def posInicialPersonagem(sprite):
    sprite.set_position(100,470)


janela = Window(1024,682)
background = GameImage("images/background_prisao.png")
personagem1 = Sprite("images/deolene.png")
personagem2 = Sprite("images/guilherme.png")
janela.set_title("FASE 1: PRISÃO")



while True:
    
    posInicialPersonagem(personagem1)
    background.draw()
    personagem1.draw()


    #personagem2.draw()
    janela.update()