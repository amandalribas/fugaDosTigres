from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
import game
import dificuldade
import personagem 
def menu():
    janela = Window(1024,682)
    jogar = GameImage("assets/buttons/buttom_jogar.png")
    dif = GameImage("assets/buttons/buttom_dificuldade.png")
    sair = GameImage("assets/buttons/buttom_sair.png")
    mouse = Window.get_mouse()
    #set position
    jogar.set_position(janela.width/2 - jogar.width/2,100)
    dif.set_position(janela.width/2 - jogar.width/2,300)
    sair.set_position(janela.width/2 - jogar.width/2,500)
    while True:
        
        janela.set_background_color([0,0,0])
        
        if (mouse.is_over_area([janela.width/2 - jogar.width/2,100], [janela.width/2 - jogar.width/2 + 300,200])) and mouse.is_button_pressed(1):
            personagem.escolha()
        if (mouse.is_over_area([janela.width/2 - jogar.width/2,300], [janela.width/2 - jogar.width/2 + 300,400])) and mouse.is_button_pressed(1):
            dificuldade.dificuldade()
        if (mouse.is_over_area([janela.width/2 - jogar.width/2,500], [janela.width/2 - jogar.width/2 + 300,600])) and mouse.is_button_pressed(1):
            janela.close()
        jogar.draw() 
        dif.draw()
        sair.draw()
        janela.update()

