import Forca
import adivinhacao

def escolhe_jogo():
    print('################################')
    print('  Escolha o jogo deseja jogar ')
    print('################################')

    print('(1) Forca (2) Adivinhação')

    jogo = int(input('Qual Jogo?: '))

    if(jogo == 1):
        print('Jogando forca')
        Forca.jogar()
    elif(jogo == 2):
        print('Jogando adivinhação')
        adivinhacao.jogar()

if(__name__ == '__main__'):
    escolhe_jogo()