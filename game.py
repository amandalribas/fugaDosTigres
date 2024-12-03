from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
import config

#fonte
pygame.font.init()
custom_font = pygame.font.Font("fonts/PressStart2P-Regular.ttf", 32)



def game():
    janela = Window(1024,682)
    teclado = Window.get_keyboard()
    background = GameImage("assets/sprites/background_prisao.png")
    background2 = GameImage("assets/sprites/background_prisao.png")
    personagem = Sprite(str(config.personagemEscolhido))
    obstaculo = Sprite(str(config.obstaculoEscolhido))
    obstaculoCopia = Sprite(str(config.obstaculoEscolhido))

    #carrinhoLimpeza = Sprite("assets/sprites/carrinholimpeza.png")
    #policial = Sprite("assets/sprites/policial.png")
    moeda = Sprite("assets/sprites/coin.png")
    janela.set_title("FASE 1: PRISÃO")
    moedas = 0
    velBackground =250
    
    personagem.set_position(110,470)
    moeda.set_position(55,35)
    obstaculo.set_position(janela.width,personagem.y + 30)

    #manipulando backgrounds
    #coloca o primeiro fundo cobrindo toda a janela
    background.x=0
    background.y=0
    #coloca o segundo fundo ao lado para servir de apoio na movimentação
    background2.x= background.width
    background2.y=0

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
            obstaculo.set_position(janela.width,personagem.y + 30)

        #carrinhoLimpeza.draw()
        background.draw()
        background2.draw()
        personagem.draw()
        obstaculo.draw()
        #policial.draw()
        texto = custom_font.render(str(moedas), True, (255,251,100))
        janela.screen.blit(texto, (130, 50)) 
        moeda.draw()

        janela.update()

