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

pygame.font.init()
custom_font = pygame.font.Font("assets/fonts/PressStart2P-Regular.ttf", 32)

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
        janela.set_title("MENU")

        janela.set_background_color([0,0,0])
        
        if (mouse.is_over_area([janela.width/2 - jogar.width/2,100], [janela.width/2 - jogar.width/2 + 300,200])) and mouse.is_button_pressed(1):
            config.velBackground = 550
            config.pontos = 0
            config.contVidas = 3
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
    background = GameImage("assets/sprites/background_personagem.png")

    deolene1 = Sprite("assets/sprites/deoleneG.png")
    guilherme1 = Sprite("assets/sprites/guilhermeG.png")
    deolene1.set_position(150,janela.height/2 - 50)
    guilherme1.set_position(janela.width-50 - 300 ,janela.height/2 - 50)
    deolene2 = Sprite("assets/sprites/deolenerunG.png",6)
    deolene2.set_total_duration(500)
    deolene2.set_position(150,janela.height/2 - 50)
    
    guilherme2 = Sprite("assets/sprites/guilhermerunG.png",6)
    guilherme2.set_total_duration(500)
    guilherme2.set_position(janela.width-50 - 300 ,janela.height/2 - 50)

    deolene = deolene1
    guilherme = guilherme1
    while True:
        janela.set_title("PERSONAGEM")
        if mouse.is_over_area([150,janela.height/2 - 50],[335,janela.height/2 + 180]):
            deolene = deolene2
            deolene.update()
            if mouse.is_button_pressed(1):
                config.personagemEscolhido = "assets/sprites/deolene.png"
                config.personagemAndando = "assets/sprites/deolenerun.png"
                config.personagemAndandoAZUL = "assets/sprites/deolenerunAZUL.png"
                config.personagemAgachando = "assets/sprites/deolenedown.png"
                config.personagemAgachandoAZUL = "assets/sprites/deoleonedownAZUL.png"
                config.p = 1
                game.main()
        if mouse.is_over_area([janela.width-50 - 300 ,janela.height/2 - 50],[janela.width-50 - 300 +185 ,janela.height/2 - 50 + 230]):
            guilherme = guilherme2
            guilherme.update()
            if mouse.is_button_pressed(1):
                config.personagemEscolhido = "assets/sprites/guilherme.png"
                config.personagemAndando = "assets/sprites/guilhermerun.png"
                config.personagemAndandoAZUL = "assets/sprites/guilhermerunAZUL.png"
                config.personagemAgachando = "assets/sprites/guilhermedown.png"
                config.personagemAgachandoAZUL = "assets/sprites/guilhermedownAZUL.png"
                config.p = 2
                game.main()

        
        background.draw()
        deolene.draw()
        guilherme.draw()
        #buttom_p1.draw()
        #buttom_p2.draw()

        nome_deolene1 = custom_font.render("deolene", True, (255, 255, 255))
        janela.screen.blit(nome_deolene1, (140,535))
        nome_deolene2 = custom_font.render("bezerro", True, (255, 255, 255))
        janela.screen.blit(nome_deolene2, (140,575))
        
        nome_gui1 = custom_font.render("guilherme", True, (255, 255, 255))
        janela.screen.blit(nome_gui1, (janela.width-50 - 300 - 20 ,535))
        nome_gui2 = custom_font.render("lime", True, (255, 255, 255))
        janela.screen.blit(nome_gui2, (janela.width-50-300 + 55,575))
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
        janela.set_title("DIFICULDADE")

        if (mouse.is_over_area([janela.width/2 - facil.width/2,150], [janela.width/2 - facil.width/2 + 300,250])) and mouse.is_button_pressed(1):
            #facil
            config.pontos = 0
            config.contVidas = 5
            config.velBackground = 500
            config.velPulo = 450
            config.dif = 1
            escolha()
        if (mouse.is_over_area([janela.width/2 - facil.width/2,350], [janela.width/2 - medio.width/2 + 300,450])) and mouse.is_button_pressed(1): 
            #medio
            config.pontos = 0
            config.contVidas = 3
            config.dif = 2
            config.velBackground = 550
            escolha()
        if (mouse.is_over_area([janela.width/2 - facil.width/2,550], [janela.width/2 - dificil.width/2 + 300,650])) and mouse.is_button_pressed(1):
            #
            config.pontos = 0
            config.contVidas = 1
            config.velBackground = 700
            config.velPulo = 600
            config.dif = 3
            escolha()

        janela.update()
        facil.draw()
        medio.draw()
        dificil.draw()
