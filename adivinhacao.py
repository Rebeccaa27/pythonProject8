import random
def jogar():
    print('################################')
    print('Bem vindo ao jogo da adivinhação')
    print('################################')

    numero_secreto = random.randrange(1, 101)
    tentativas = 0
    pontos = 1000

    nome = input('Olá jogador(a), qual é o seu nome? ')
    print('Oi {}, qual nível de dificuldade deseja jogar ?'.format(nome))
    print('(1) Fácil (2) Médio (3) Difícil')

    nivel = int(input('Defina o nível: '))

    if (nivel == 1):
        tentativas = 20
    elif (nivel == 2):
        tentativas = 10
    else:
        tentativas = 5

    for rodada in range(1, tentativas + 1):
        print('Tentativas {} de {}'.format(rodada, tentativas))

        chute_str = int(input('Digite um número entre 1 a 100:  '))
        print('Você digitou', chute_str)
        chute = int(chute_str)

        if (chute < 1 or chute > 100):
            print('Você deve digitar um número de 1 a 100 ')
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print('Você acertou e fez {} pontos!'.format(pontos))
            break
        else:
            if (maior):
                print('Você errou! O seu chute foi maior do que o número secreto.')
            elif (menor):
                print('Você errou! O seu chute foi menor do que o número secreto.')
                pontos_perdidos = abs(numero_secreto - chute)
                pontos = pontos - pontos_perdidos

    print('Fim de jogo!.')

if(__name__ == ' __main__'):
 jogar()