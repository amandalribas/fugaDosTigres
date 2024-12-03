from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
import game
import personagem 
import config 

def dificuldade():
    janela = Window(1024,682)
    facil = GameImage("assets/buttons/buttom_facil.png")
    medio = GameImage("assets/buttons/buttom_medio.png")
    dificil = GameImage("assets/buttons/buttom_dificil.png")
    facil.set_position(janela.width/2 - facil.width/2,150)
    medio.set_position(janela.width/2 - medio.width/2,350)
    dificil.set_position(janela.width/2 - dificil.width/2,550)
    mouse = Window.get_mouse()
    while True:
        if (mouse.is_over_area([janela.width/2 - facil.width/2,150], [janela.width/2 - facil.width/2 + 300,250])) and mouse.is_button_pressed(1): 
            personagem.escolha()
        if (mouse.is_over_area([janela.width/2 - facil.width/2,350], [janela.width/2 - medio.width/2 + 300,450])) and mouse.is_button_pressed(1):
            config.dif_lvl = 2
            personagem.escolha()
        if (mouse.is_over_area([janela.width/2 - facil.width/2,550], [janela.width/2 - dificil.width/2 + 300,650])) and mouse.is_button_pressed(1):
            config.dif_lvl = 3
            personagem.escolha()

        janela.update()
        facil.draw()
        medio.draw()
        dificil.draw()
