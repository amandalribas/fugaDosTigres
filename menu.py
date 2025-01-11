from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
import config
import game

# som
pygame.mixer.init()
som = pygame.mixer.Sound("assets/sounds/balada.wav")
music_channel = pygame.mixer.Channel(0)

music_channel.play(som, loops=-1)

def main():
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
            escolha()
        if (mouse.is_over_area([janela.width/2 - jogar.width/2,300], [janela.width/2 - jogar.width/2 + 300,400])) and mouse.is_button_pressed(1):
            dificuldade()
        if (mouse.is_over_area([janela.width/2 - jogar.width/2,500], [janela.width/2 - jogar.width/2 + 300,600])) and mouse.is_button_pressed(1):
            janela.close()
        jogar.draw() 
        dif.draw()
        sair.draw()
        janela.update()

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
            config.personagemAndando = "assets/sprites/deolenerun.png"
            config.p = 1
            game.main()
        if (mouse.is_over_area([janela.width-50 - buttom_p1.width,janela.height/2 - buttom_p1.height/2], [janela.width-50 - buttom_p1.width + 300,janela.height/2 - buttom_p1.height/2 + 100])) and mouse.is_button_pressed(1):
            config.personagemEscolhido = "assets/sprites/guilherme.png"
            config.p = 2
            game.main()
        buttom_p1.draw()
        buttom_p2.draw()
        janela.update()



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
            #facil
            config.contVidas = 5
            config.velBackground = 500
            config.velPulo = 450
            escolha()
        if (mouse.is_over_area([janela.width/2 - facil.width/2,350], [janela.width/2 - medio.width/2 + 300,450])) and mouse.is_button_pressed(1): 
            #medio
            escolha()
        if (mouse.is_over_area([janela.width/2 - facil.width/2,550], [janela.width/2 - dificil.width/2 + 300,650])) and mouse.is_button_pressed(1):
            #
            config.contVidas = 1
            config.velBackground = 700
            config.velPulo = 600
            escolha()

        janela.update()
        facil.draw()
        medio.draw()
        dificil.draw()
