# JOGOS-SIMPLES
import pygame
from random import randint
from time import sleep
from termcolor import colored

Jogo = ['PEDRA', 'PAPEL', 'TESOURA']
cont_de_partidas = [0]
cont_de_vitorias = [0]
cont_de_derrotas = [0]
cont_de_empates = [0]
print(colored('PEDRA PAPEL E TESOURA', 'magenta'))
pygame.init()
pygame.mixer.music.load('C:/Users/abraa\OneDrive\Documentos/voz-do-narrador/escript.mp3')
pygame.mixer.music.play(1)

while True:
    # PARTE VISUAL
    print(colored('-' * 30, 'green'))
    print(colored('SUAS OPÇÕES:\n[0] PEDRA\n[1] PAPEL\n[2] TESOURA', 'yellow'))
    print(colored('-' * 30, 'green'))
    #  ESCOLHA DE JOGADAS
    Jogador = int(input('Digite sua Opção: '))
    CPU = randint(0, 2)
    resposta = ' '
    # CONDIÇÕES
    if Jogador <= 2 and Jogador >= 0:
        cont_de_partidas.append(1)
        # MOSTRAR ESCOLHAS
        pygame.init()
        pygame.mixer.music.load('C:/Users/abraa\OneDrive\Documentos/voz-do-narrador/ppt.mp3')
        pygame.mixer.music.play(1)
        print(colored('>PEDRA', 'magenta'))
        sleep(0.4)
        print(colored('<PAPEL', 'cyan'))
        sleep(0.4)
        print(colored('>TESOURA...', 'grey'))
        sleep(0.6)
        print(colored('-' * 30, 'green'))
        sleep(0.5)
        print(f'O Jogador escolheu: {Jogo[Jogador]}\nO Computador escolheu: {Jogo[CPU]}', end='\n')
        # AUDIOS - JOGADOR
        if Jogador == 0:
            pygame.init()
            pygame.mixer.music.load('C:/Users/abraa\OneDrive\Documentos/voz-do-narrador/o-jogador-jogou-pedra.mp3')
            pygame.mixer.music.play(1)
            sleep(2)
        elif Jogador == 1:
            pygame.init()
            pygame.mixer.music.load('C:/Users/abraa\OneDrive\Documentos/voz-do-narrador/o-jogador-jogou-papel.mp3')
            pygame.mixer.music.play(1)
            sleep(2)
        else:
            pygame.init()
            pygame.mixer.music.load('C:/Users/abraa\OneDrive\Documentos/voz-do-narrador/o-jogador-jogou-tesoura.mp3')
            pygame.mixer.music.play(1)
            sleep(2)
        # AUDIOS - CPU
        if CPU == 0:
            pygame.init()
            pygame.mixer.music.load('C:/Users/abraa\OneDrive\Documentos/voz-do-narrador/o-computador-jogou-pedra.mp3')
            pygame.mixer.music.play(1)
            sleep(2.5)
        elif CPU == 1:
            pygame.init()
            pygame.mixer.music.load('C:/Users/abraa\OneDrive\Documentos/voz-do-narrador/o-computador-jogou-papel.mp3')
            pygame.mixer.music.play(1)
            sleep(2.5)
        else:
            pygame.init()
            pygame.mixer.music.load('C:/Users/abraa\OneDrive\Documentos/voz-do-narrador/o-computador-jogou-tesoura.mp3')
            pygame.mixer.music.play(1)
            sleep(2.5)
            # EMPATE
        if Jogador == CPU:
            cont_de_empates.append(1)
            print(colored('Empate.', 'blue'))
            pygame.init()
            pygame.mixer.music.load('C:/Users/abraa\OneDrive\Documentos/voz-do-narrador/deu-empate-.mp3')
            pygame.mixer.music.play(1)
            sleep(2)
            # VITÓRIA DO JOGADOR
        elif Jogador == 0 and CPU == 2 or Jogador == 1 and CPU == 0 or Jogador == 2 and CPU == 1:
            cont_de_vitorias.append(1)
            print(colored('O Jogador Venceu.', 'yellow'))
            pygame.init()
            pygame.mixer.music.load('C:/Users/abraa\OneDrive\Documentos/voz-do-narrador/o-jogador-venceu.mp3')
            pygame.mixer.music.play(1)
            sleep(2)
            # VITÓRIA DO CPU
        elif CPU == 0 and Jogador == 2 or CPU == 1 and Jogador == 0 or CPU == 2 and Jogador == 1:
            cont_de_derrotas.append(1)
            print(colored('O Computador Venceu.', 'red'))
            pygame.init()
            pygame.mixer.music.load('C:/Users/abraa\OneDrive\Documentos/voz-do-narrador/o-computador-venceu.mp3')
            pygame.mixer.music.play(1)
            sleep(2)
    else:
        print(colored('Opção Inválida, tente novamente.', 'red'))
        pygame.init()
        pygame.mixer.music.load('C:/Users/abraa\OneDrive\Documentos/voz-do-narrador/opcao-.mp3')
        pygame.mixer.music.play(1)
        sleep(4)
    # PARAR OU CONTINUAR
    while resposta not in 'SN':
        print(colored('-' * 30, 'green'))
        pygame.init()
        pygame.mixer.music.load('C:/Users/abraa\OneDrive\Documentos/voz-do-narrador/voce.mp3')
        pygame.mixer.music.play(1)
        resposta = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    if resposta == 'N':
        pygame.init()
        pygame.mixer.music.load('C:/Users/abraa\OneDrive\Documentos/voz-do-narrador/fim-.mp3')
        pygame.mixer.music.play(1)
        sleep(3.5)
        break
print(colored('-' * 30, 'green'))
print(colored('PLACAR:', 'yellow'))
print(colored('-' * 30, 'green'))
print(colored(f'Partidas Jogadas: {sum(cont_de_partidas)}'
              f'\nVitória (s): {sum(cont_de_vitorias)}'
              f'\nDerrota (s): {sum(cont_de_derrotas)}'
              f'\nEmpate (s): {sum(cont_de_empates)}', 'yellow'))
print(colored('-' * 30, 'green'))
print(colored(f'O JOGO ACABOU!', 'red'))
print(colored('-' * 30, 'green'))
