import menu
from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.animation import *
import config
import random
import pygame


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

    menu.music_channel.stop()
    fim_channel.play(s_gameOver)

    while True:
        janela.draw_text("GAME-OVER", 335, janela.height / 2, size=70, color=(255, 0, 0), font_name="Arial", bold=False, italic=False)
        if teclado.key_pressed("esc"):
            janela.close()
        janela.update()
