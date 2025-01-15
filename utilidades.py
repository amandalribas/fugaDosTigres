import menu
from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.animation import *
import config
import random
import pygame
import menu
import os
import rank

pygame.mixer.init()
s_pulo = pygame.mixer.Sound("assets/sounds/jump.wav")
s_colide = pygame.mixer.Sound("assets/sounds/S_colide.wav")
s_moeda = pygame.mixer.Sound("assets/sounds/S_moeda.wav")
s_gameOver = pygame.mixer.Sound("assets/sounds/S_gameOver.wav")
s_win = pygame.mixer.Sound("assets/sounds/win_sound.wav")

pulo_channel = pygame.mixer.Channel(1)
moeda_channel = pygame.mixer.Channel(2)
colide_channel = pygame.mixer.Channel(3)
fim_channel = pygame.mixer.Channel(4)
win_channel = pygame.mixer.Channel(5)

pygame.font.init()
custom_font = pygame.font.Font("assets/fonts/PressStart2P-Regular.ttf", 32)

# CONFIGURANDO O ESCUDO -------------------
def powerUpEscudo(escudo, janela, personagemAndando, invencivel):
    escudo.x -= config.velBackground * janela.delta_time()

    if escudo.x < -escudo.width:
        escudo.set_position(-500, -500)

    if personagemAndando.collided(escudo):
        escudo.set_position(-500, -500)
        invencivel = True
        if config.p == 1:
            personagemAndando = Sprite("assets/sprites/deolenerunAZUL.png",6)
        elif config.p == 2:
            personagemAndando = Sprite("assets/sprites/guilhermerunAZUL.png",6)
        personagemAndando.set_total_duration(500)
        personagemAndando.set_position(110, 470)

    return invencivel, personagemAndando

# DUPLICADOR DE MOEDAS -------------------
def doubleCoins(duplica_coins, janela, personagemAndando, contMoedas):
    duplica_coins.x -= config.velBackground * janela.delta_time()

    if duplica_coins.x < -duplica_coins.width:
        duplica_coins.set_position(-500, -500)

    if personagemAndando.collided(duplica_coins):
        duplica_coins.set_position(-500, -500)
        contMoedas = (contMoedas * 2) + 1
        moeda_channel.play(s_moeda)

    return contMoedas

def gameover():
    janela = Window(1024, 682)
    teclado = Window.get_keyboard()
    mouse = Window.get_mouse()
    janela.set_title("GAME-OVER")
    background = GameImage("assets/sprites/background_gameover.png")
    menu.music_channel.stop()
    fim_channel.play(s_gameOver)
    buttom_sim = GameImage("assets/buttons/buttom_sim.png")
    buttom_sim.set_position(332,400)
    buttom_sim_pressed = GameImage("assets/buttons/buttom_sim_pressed.png")
    buttom_sim_pressed.set_position(332,400)
    buttom_s = buttom_sim

    buttom_nao = GameImage("assets/buttons/buttom_nao.png")
    buttom_nao.set_position(532,400)
    buttom_nao_pressed = GameImage("assets/buttons/buttom_nao_pressed.png")
    buttom_nao_pressed.set_position(532,400)
    buttom_n = buttom_nao
    while True:
        janela.draw_text("GAME-OVER", 335, janela.height / 2, size=70, color=(255, 0, 0), font_name="Arial", bold=False, italic=False)
        if teclado.key_pressed("esc"):
            janela.close()
        if mouse.is_over_area([332,400],[482,500]):
            buttom_s = buttom_sim_pressed
            if mouse.is_button_pressed(1):
                menu.main()
        else:
            buttom_s = buttom_sim
        if mouse.is_over_area([532,400],[682,500]):
            buttom_n = buttom_nao_pressed
            if mouse.is_button_pressed(1):
                janela.close()
        else:
            buttom_n = buttom_nao
        background.draw()
        buttom_s.draw()
        buttom_n.draw()
        janela.update()

def win():
    janela = Window(1024, 682)
    teclado = Window.get_keyboard()
    mouse = Window.get_mouse()

    janela.set_title("VOCE GANHOU!")
    background = GameImage("assets/sprites/background_venceu.png")

    menu.music_channel.stop()
    win_channel.play(s_win)

    buttom_sim = GameImage("assets/buttons/buttom_sim.png")
    buttom_sim.set_position(282,400)
    buttom_sim_pressed = GameImage("assets/buttons/buttom_sim_pressed.png")
    buttom_sim_pressed.set_position(282,400)
    buttom_s = buttom_sim

    buttom_nao = GameImage("assets/buttons/buttom_nao.png")
    buttom_nao.set_position(582,400)
    buttom_nao_pressed = GameImage("assets/buttons/buttom_nao_pressed.png")
    buttom_nao_pressed.set_position(582,400)
    buttom_n = buttom_nao

    while True:
        if teclado.key_pressed("esc"):
            janela.close()
        if mouse.is_over_area([282,400],[532,500]):
            buttom_s = buttom_sim_pressed
            if mouse.is_button_pressed(1):
                menu.main()
        else:
            buttom_s = buttom_sim
        if mouse.is_over_area([582,400],[732,500]):
            buttom_n = buttom_nao_pressed
            if mouse.is_button_pressed(1):
                janela.close()
        else:
            buttom_n = buttom_nao
        background.draw()
        buttom_s.draw()
        buttom_n.draw()
        janela.update()


def exibir_ranking(janela):
    ranking = []
    arquivo = "classifica.txt"
    teclado = Window.get_keyboard()

    # Lê o arquivo de ranking, se existir
    if os.path.exists(arquivo):
        with open(arquivo, "r") as f:
            for linha in f:
                dados = linha.strip().split(",")
                ranking.append((dados[0], int(dados[1])))

    # Ordena o ranking do maior para o menor
    ranking = sorted(ranking, key=lambda x: x[1], reverse=True)

    # Adiciona a imagem de fundo
    janela.set_background_color((0, 0, 255))
    while True:

        # Exibir o ranking na tela
        #janela.draw_text("Ranking", janela.width / 2 - 50, 50, size=40, color=(255, 255, 255), font_name="Arial",
                         #bold=True)
        ranking_nome = custom_font.render("RANKING: ", True, (255, 255, 255))
        janela.screen.blit(ranking_nome, ((janela.width / 2)-100, 50))
        y_pos = 150
        for i, (nome, pontos) in enumerate(ranking[:5]):  # Mostra até os 5 melhores
            nomes = custom_font.render(f"{i + 1}. {nome}: {pontos} pontos", True, (255, 255, 255))
            janela.screen.blit(nomes, (150, y_pos))
            y_pos += 100
        if teclado.key_pressed("esc"):
            menu.main()
        janela.update()
