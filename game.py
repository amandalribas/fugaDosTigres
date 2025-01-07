from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
import config
import random

#fonte
pygame.font.init()
custom_font = pygame.font.Font("assets/fonts/PressStart2P-Regular.ttf", 32)

def gameover():
    janela = Window(1024,682)
    teclado = Window.get_keyboard()

    while True:
        janela.draw_text("GAME-OVER", 335, janela.height/2, size=70, color=(255,0,0), font_name="Arial", bold=False, italic=False)
        if (teclado.key_pressed("esc")):
            janela.close()
        janela.update()

def main():
    config.contVidas += 1

    janela = Window(1024,682)
    teclado = Window.get_keyboard()
    background = GameImage("assets/sprites/background_prisao.png")
    background2 = GameImage("assets/sprites/background_prisao.png")
    personagem = Sprite(str(config.personagemEscolhido))
    
    moedaJogo = Sprite("assets/sprites/coinG.png")
    yPersonagemInicial = 470
    personagem.set_position(110,yPersonagemInicial)

    listaObstaculos = ["assets/sprites/carrinholimpeza.png", "assets/sprites/policial.png", "assets/sprites/mesa.png", "assets/sprites/bala.png"]
    posicoesObstaculos = [personagem.y + 15, personagem.y + 15, personagem.y + 100, personagem.y + 35]
    atual = random.randint(0,(len(listaObstaculos)-1))
    obstaculo = Sprite(str(listaObstaculos[atual]))
    obstaculo.set_position(janela.width + 300,posicoesObstaculos[atual])
    
    moeda = Sprite("assets/sprites/coin.png")
    moeda.set_position(55,35)

    vida = Sprite("assets/sprites/vida.png")
    vida.set_position(janela.width - 110,35)


    janela.set_title("FASE 1: PRISÃO")
    
    contMoedas = 0
        
    contLooping = 0
    #MANIPULANDO BACKGROUNDS
    #coloca o primeiro fundo cobrindo toda a janela
    background.x=0
    background.y=0
    #coloca o segundo fundo ao lado para servir de apoio na movimentação
    background2.x= background.width
    background2.y=0
    
    #PULO
    sobe = False
    pulo = False

    moedaJogo.set_position(janela.width + obstaculo.width/2,personagem.y - 180)
    colidiu = False
    while True:
        #posicioes Iniciais:
        #obstaculoInicial(carrinhoLimpeza)
        
        #movimenta ambos para a esquerda
        background.x-= config.velBackground*janela.delta_time()
        background2.x-= config.velBackground*janela.delta_time()
        obstaculo.x-= config.velBackground*janela.delta_time()
    
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


        #MOEDA        
        if contLooping == 2:
            moedaJogo.x-= config.velBackground*janela.delta_time()
            if moedaJogo.x < moedaJogo.width:
                moedaJogo.set_position(janela.width + obstaculo.width/3 + 20, yPersonagemInicial - 180)
                contLooping = 0
        if personagem.collided_perfect(moedaJogo):
            moedaJogo.set_position(-500,-500)
            contMoedas += 1

        #PERSONAGEM PERDENDO VIDAS AO COLIDIR:
        if personagem.collided_perfect(obstaculo):
            colidindo = True
            colidiu = True
        else:
            colidindo = False
        if not(colidindo) and colidiu:
            config.contVidas -= 1
            colidiu = False
        if config.contVidas == 0:
            gameover()

        #PULO
        if not(pulo) and teclado.key_pressed("space"):
            sobe = True
            pulo = True
        if sobe and personagem.y > 200: #personagem sobe até a altura 200
            personagem.move_y(-config.velPulo*janela.delta_time()) 
        if 190 <= personagem.y <= 200: #se atinge a altura limite para de subir
            sobe = False
        if not(sobe) and personagem.y < 470: #se ja atingiu a altura limite, desce, até chegar no chao
            personagem.move_y(config.velPulo*janela.delta_time())   
        if 470 <= personagem.y <= 480: #se está no chão, não está pulando, cooldown 
            pulo = False
        #print(personagem.y)
            

        #carrinhoLimpeza.draw()
        background.draw()
        background2.draw()
        personagem.draw()
        obstaculo.draw()
        #policial.draw()
        textoMoedas = custom_font.render(str(contMoedas), True, (255,251,100))
        janela.screen.blit(textoMoedas, (130, 50)) 
        textoVidas = custom_font.render(str(config.contVidas), True, (255,251,100))
        janela.screen.blit(textoVidas, (janela.width - 160,50))
        moeda.draw()
        moedaJogo.draw()
        vida.draw()
        janela.update()
