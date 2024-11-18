from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *

janela = Window(1024,682)
background = GameImage("images/background_prisao.png")
personagem1 = Sprite("images/deolene.png")
personagem2 = Sprite("images/guilherme.png")

while True:
    
    personagem1.set_position(200, 300)
    background.draw()
    personagem1.draw()
    #personagem2.draw()
    janela.update()