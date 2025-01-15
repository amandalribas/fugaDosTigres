import pygame

import utilidades

# Inicializa o Pygame
pygame.init()


# Função para capturar o nome do jogador
def input_nome(screen,controle_ranking, pontua):
    #Criando a caixa de texto e deixando mais "bonitinha"
    font = pygame.font.Font("assets/fonts/PressStart2P-Regular.ttf", 32)
    input_box = pygame.Rect(screen.get_width() // 2 - 200, screen.get_height() // 2 - 50, 400, 80)
    color_inactive = pygame.Color('gray')
    color_active = pygame.Color('white')
    color = color_inactive
    active = False
    text = ''
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        salvar_classificacao(text, pontua)
                        if controle_ranking==1:
                            utilidades.gameover()
                        else:
                            utilidades.win()
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        screen.fill((0, 0, 255))

        #escrevendo na tela
        title_font = pygame.font.Font("assets/fonts/PressStart2P-Regular.ttf", 40)
        title_surface = title_font.render("Digite seu nome: ", True, (255, 0, 0))
        title_rect = title_surface.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 - 100))
        screen.blit(title_surface, title_rect)

        #Configurações para que o usuário consiga ver o que está digitando na caixa de texto
        txt_surface = font.render(text, True, (255, 255, 255))
        input_box.center = (screen.get_width() // 2, screen.get_height() // 2)
        input_box.w = max(400,txt_surface.get_width() + 10)
        screen.blit(txt_surface, (input_box.x + (input_box.w - txt_surface.get_width()) // 2, input_box.y + 25))
        pygame.draw.rect(screen, color, input_box, 4)
        pygame.display.flip()



# Função para salvar o nome e os pontos no arquivo
def salvar_classificacao(nome, pontua):
    with open("classifica.txt", "a") as arquivo:
        arquivo.write(f"{nome},{int(pontua)}\n")


# Função principal
def main(controle_ranking, pontua):
    screen = pygame.display.set_mode((1024, 682))
    pygame.display.set_caption('Salvar pontuação')

    input_nome(screen,controle_ranking, pontua)  # Captura o nome do jogador

    screen.fill((0, 0, 255))
    pygame.display.flip()
