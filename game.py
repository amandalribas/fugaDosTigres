import menu
from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.animation import *
import config
import random
import pygame
import utilidades

# fonte
pygame.font.init()
custom_font = pygame.font.Font("assets/fonts/PressStart2P-Regular.ttf", 32)

# efeitos sonoros
pygame.mixer.init()
s_pulo = pygame.mixer.Sound("assets/sounds/jump.wav")
s_colide = pygame.mixer.Sound("assets/sounds/S_colide.wav")
s_moeda = pygame.mixer.Sound("assets/sounds/S_moeda.wav")
s_gameOver = pygame.mixer.Sound("assets/sounds/S_gameOver.wav")

# criando canais separados para o fundo e os efeitos (evitando conflito)
pulo_channel = pygame.mixer.Channel(1)
moeda_channel = pygame.mixer.Channel(2)
colide_channel = pygame.mixer.Channel(3)
fim_channel = pygame.mixer.Channel(4)


def main():
    janela = Window(1024, 682)
    teclado = Window.get_keyboard()
    background = GameImage("assets/sprites/background_prisao.png")
    background2 = GameImage("assets/sprites/background_prisao.png")

    personagemAndando = Sprite(str(config.personagemAndando), 6)
    personagemAndando.set_total_duration(500)
    personagemAndandoAZUL = Sprite(str(config.personagemAndandoAZUL),6)
    personagemAndandoAZUL.set_total_duration(500)
    personagemAndandoAZUL.set_position(110, 470)

    personagemAgachando = Sprite(str(config.personagemAgachando),6)
    personagemAgachando.set_total_duration(500)
    personagemAgachandoAZUL = Sprite(str(config.personagemAgachandoAZUL),6)
    personagemAgachandoAZUL.set_total_duration(500)
    personagemAgachandoAZUL.x = 110

    personagem = personagemAndando
    moedaJogo = Sprite("assets/sprites/coinG.png")
    yPersonagemInicial = 470

    personagem.set_position(110, yPersonagemInicial)

    listaObstaculos = ["assets/sprites/carrinholimpeza.png", "assets/sprites/policial.png", "assets/sprites/mesa.png", "assets/sprites/bala.png"]
    posicoesObstaculos = [personagem.y + 15, personagem.y + 15, personagem.y + 100, personagem.y - 25]
    atual = random.randint(0, (len(listaObstaculos) - 1))
    obstaculo = Sprite(str(listaObstaculos[atual]))

    moeda = Sprite("assets/sprites/coin.png")
    moeda.set_position(55, 35)

    vida = Sprite("assets/sprites/vida.png")
    vida.set_position(janela.width - 150, 0)

    escudo = Sprite("assets/sprites/escudo.png")
    escudo.set_position(-500, -500)

    duplica_coins = Sprite("assets/sprites/duplicador_coin.png")
    duplica_coins.set_position(-500, -500)

    janela.set_title("FASE 1: PRISÃO")

    #POWER UPS --------------- variaveis
    contMoedas = 0
    contLooping = 0
    contLoopingEscudo = 0
    escudo_ativo = False

    #MANIPULANDO BACKGROUNDS ---------------
    #coloca o primeiro fundo cobrindo toda a janela
    background.x = 0
    background.y = 0
    #coloca o segundo fundo ao lado para servir de apoio na movimentação
    background2.x = background.width
    background2.y = 0

    #PULO --------- variaveis
    sobe = False
    pulo = False

    # Controles
    controle_power_up = False
    invencivel = False
    colidiu = False

    ##
    multiPontos = 0.01
    moedaJogo.set_position(janela.width + obstaculo.width / 2, personagem.y - 180)
    obst = 0
    fase2 = False
    while True:
        # MOVIMENTACAO DO BACKGROUND + OBSTACULO ---------------
        # movimenta ambos para a esquerda
        background.x -= config.velBackground * janela.delta_time()
        background2.x -= config.velBackground * janela.delta_time()
        obstaculo.x -= config.velBackground * janela.delta_time()

        # vai fazendo a movimentação "circular"
        if background.x + background2.width <= 0:
            background.x = background2.x + background2.width
        if background2.x + background2.width <= 0:
            background2.x = background.x + background.width

        #repete o obstaculo
        if obstaculo.x < -(obstaculo.width):
            atual = random.randint(0, (len(listaObstaculos) - 1))
            if fase2 and atual == 3:
                obstaculo = Sprite(str(listaObstaculos[atual]),8)
                obstaculo.set_total_duration(500)
            else:
                obstaculo = Sprite(str(listaObstaculos[atual]))
            obstaculo.set_position(janela.width, posicoesObstaculos[atual])
            if fase2 and obst == 0:
                obstaculo = Sprite(str(listaObstaculos[1]))
                obstaculo.set_position(janela.width, posicoesObstaculos[1])
            contLooping += 1
            contLoopingEscudo += 1
            obst = obst + 1

        #MOEDA ----------------------
        if (contLooping == 2) and not controle_power_up:
            moedaJogo.x -= config.velBackground * janela.delta_time()
            if moedaJogo.x < moedaJogo.width:
                moedaJogo.set_position(janela.width + obstaculo.width / 3 + 20, yPersonagemInicial - 180)
                contLooping = 0

        if personagem.collided(moedaJogo):
            moedaJogo.set_position(-500, -500)
            contMoedas += 1
            moeda_channel.play(s_moeda)
            if contMoedas > 1:
                multiPontos = 0.01 * contMoedas

        #MOEDA DUPLICADORA -------------------
        if contMoedas % 7 == 0 and contMoedas != 0:
            duplica_coins.set_position(janela.width + 70, yPersonagemInicial - 180)

        contMoedas = utilidades.doubleCoins(duplica_coins, janela, personagem, contMoedas)

        #ESCUDO -------------------
        if not escudo_ativo and contLoopingEscudo >= 14 or teclado.key_pressed('7'):
            escudo_ativo = True
            contLoopingEscudo = 0
            escudo.set_position(janela.width/2 + 40, 510)

        if escudo_ativo:
            invencivel, personagem = utilidades.powerUpEscudo(escudo, janela, personagem, invencivel)
            if escudo.x < -escudo.width:
                escudo_ativo = False
                escudo.set_position(-500, -500)

        #PERSONAGEM PERDENDO VIDAS AO COLIDIR ---------------
        if personagem.collided(obstaculo):
            if invencivel:
                invencivel = False
                obstaculo.set_position(-500, -500)
                personagem = personagemAndando
                personagem.set_position(110, yPersonagemInicial)
            else:
                colidindo = True
                colidiu = True
        else:
            colidindo = False

        if not colidindo and colidiu:
            if not escudo_ativo:
                config.contVidas -= 1
                colidiu = False
                colide_channel.play(s_colide)

        if config.contVidas == 0:
            utilidades.gameover()

        #PULO ---------------------------
        if not pulo and teclado.key_pressed("up") and not(teclado.key_pressed("down")):
            sobe = True
            pulo = True
        if sobe and personagem.y > 110:  #personagem sobe até a altura 200
            personagem.move_y(-config.velPulo * janela.delta_time())
            pulo_channel.play(s_pulo)
        if 10 <= personagem.y <= 120: #se atinge a altura limite para de subir
            sobe = False
        if not sobe and personagem.y < 470:  #se ja atingiu a altura limite, desce, até chegar no chao
            personagem.move_y(config.velPulo * janela.delta_time())
        if 470 <= personagem.y <= 480: #se está no chão, não está pulando, cooldown
            pulo = False
        
        #AGACHANDOO ------------------------
        if not (pulo):
            if teclado.key_pressed("down"):
                personagemAgachando.set_position(personagem.x,personagem.y)
                agachou = True
                if invencivel and agachou:
                    personagem = personagemAgachandoAZUL               
                elif agachou:
                    personagem = personagemAgachando
                personagem.y = yPersonagemInicial + 28
            elif not(invencivel):
                personagem = personagemAndando
                personagem.y = yPersonagemInicial
            elif invencivel:
                personagem = personagemAndandoAZUL
        agachou = False

        #PONTOS --------------------
        config.pontos += multiPontos

        # Movimento da moeda
        moedaJogo.x -= config.velBackground * janela.delta_time()  # Moeda se movendo para a esquerda

        if moedaJogo.x < -moedaJogo.width:  # Moeda saiu da tela
            moedaJogo.set_position(-500, -500)


        ########### PROXIMA FASE:::
        if not(fase2) and (obst > 2 or teclado.key_pressed('2')):
            listaObstaculos = ["assets/sprites/carro.png", "assets/sprites/Bush_18.png", "assets/sprites/cone.png", "assets/sprites/bird.png"]
            fase2 = True
            obst = 0
            posicoesObstaculos = [yPersonagemInicial + 10, yPersonagemInicial + 50, yPersonagemInicial + 15, yPersonagemInicial - 40]
            
            antigox1 = background.x
            antigox2 = background2.x

            background = GameImage("assets/sprites/background_fase2.png")
            background.x = antigox1
            background2 = GameImage("assets/sprites/background_fase2_parallax.png")
            background2.x = antigox2
            janela.update()
            if config.dif == 1:
                config.velBackground = 550
            elif config.dif == 2:
                config.velBackground = 600
            elif config.dif == 3:
                config.velBackground = 750
            

        if fase2 and (obst > 25 or teclado.key_pressed('3')):
            utilidades.win()

        # UPDATES, TEXTO, DRAW ---------
        background.draw()
        background2.draw()
        personagem.draw()
        obstaculo.draw()

        textoMoedas = custom_font.render(str(contMoedas), True, (255, 251, 100))
        janela.screen.blit(textoMoedas, (130, 50))
        textoVidas = custom_font.render(str(config.contVidas), True, (255, 251, 100))
        janela.screen.blit(textoVidas, (janela.width - 160, 50))
        textoPontos = custom_font.render(str(int(config.pontos)), True, (255, 255, 255))
        janela.screen.blit(textoPontos, (janela.width // 2 - 45, 50))
        moeda.draw()
        moedaJogo.draw()
        escudo.draw()
        vida.draw()
        duplica_coins.draw()
        if fase2 and atual == 3 and obst > 0:
            obstaculo.update()
        personagem.update()
        janela.update()


#main()
