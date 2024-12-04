from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
import config
import random


#fonte
pygame.font.init()
custom_font = pygame.font.Font("assets/fonts/PressStart2P-Regular.ttf", 32)

def game():
    janela = Window(1024,682)
    teclado = Window.get_keyboard()
    background = GameImage("assets/sprites/background_prisao.png")
    background2 = GameImage("assets/sprites/background_prisao.png")
    personagem = Sprite(str(config.personagemEscolhido))
    
    moedaJogo = Sprite("assets/sprites/coinG.png")
    personagem.set_position(110,470)

    listaObstaculos = ["assets/sprites/carrinholimpeza.png", "assets/sprites/policial.png", "assets/sprites/mesa.png", "assets/sprites/bala.png"]
    posicoesObstaculos = [personagem.y + 15, personagem.y + 15, personagem.y + 100, personagem.y + 35]
    atual = random.randint(0,(len(listaObstaculos)-1))
    obstaculo = Sprite(str(listaObstaculos[atual]))
    obstaculo.set_position(janela.width,posicoesObstaculos[atual])
    
    moeda = Sprite("assets/sprites/coin.png")
    janela.set_title("FASE 1: PRISÃO")
    
    moedas = 0
    velBackground =350
    
    moeda.set_position(55,35)
    
    contLooping = 0
    #manipulando backgrounds
    #coloca o primeiro fundo cobrindo toda a janela
    background.x=0
    background.y=0
    #coloca o segundo fundo ao lado para servir de apoio na movimentação
    background2.x= background.width
    background2.y=0


    moedaJogo.set_position(janela.width + obstaculo.width/2,personagem.y - 180)
    while True:
        #posicioes Iniciais:
        #obstaculoInicial(carrinhoLimpeza)
        
        #movimenta ambos para a esquerda
        background.x-= velBackground*janela.delta_time()
        background2.x-= velBackground*janela.delta_time()
        obstaculo.x-= velBackground*janela.delta_time()
    
        #vai fazendo a movimentação "circular"
        if background.x + background2.width <= 0:
            background.x = background2.x + background2.width
        if background2.x + background2.width <= 0:
            background2.x = background.x + background.width
            
        #repete o obstaculo
        if obstaculo.x < -(obstaculo.width):
            atual = random.randint(0,(len(listaObstaculos)-1))
            obstaculo = Sprite(str(listaObstaculos[atual]))
            obstaculo.set_position(janela.width,posicoesObstaculos[atual])
            contLooping += 1
        #moeda aparecendo
        
        moedaJogo.hide()
        if contLooping == 2:
            moedaJogo.unhide()
            moedaJogo.x-= velBackground*janela.delta_time()
            if moedaJogo.x < moedaJogo.width:
                moedaJogo.set_position(janela.width + obstaculo.width/2,personagem.y - 180)
                contLooping = 0


        #carrinhoLimpeza.draw()
        background.draw()
        background2.draw()
        personagem.draw()
        obstaculo.draw()
        #policial.draw()
        texto = custom_font.render(str(moedas), True, (255,251,100))
        janela.screen.blit(texto, (130, 50)) 
        moeda.draw()
        moedaJogo.draw()
        janela.update()

game()