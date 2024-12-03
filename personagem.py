from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
import game
import config

def escolha():
    janela = Window(1024,682)
    mouse = Window.get_mouse()
    buttom_p1 = GameImage("assets/buttons/buttom_P1.png")
    buttom_p2 = GameImage("assets/buttons/buttom_P2.png")
    buttom_p1.set_position(50,janela.height/2 - buttom_p1.height/2)
    buttom_p2.set_position(janela.width-50 - buttom_p1.width ,janela.height/2 - buttom_p1.height/2)

    while True:
        
        if (mouse.is_over_area([50,janela.height/2 - buttom_p1.height/2], [350,janela.height/2 - buttom_p1.height/2 + 100])) and mouse.is_button_pressed(1):
            config.personagemEscolhido = "assets/sprites/deolene.png"
            game.game()
        if (mouse.is_over_area([janela.width-50 - buttom_p1.width,janela.height/2 - buttom_p1.height/2], [janela.width-50 - buttom_p1.width + 300,janela.height/2 - buttom_p1.height/2 + 100])) and mouse.is_button_pressed(1):
            config.personagemEscolhido = "assets/sprites/guilherme.png"
            game.game()
        buttom_p1.draw()
        buttom_p2.draw()
        janela.update()

