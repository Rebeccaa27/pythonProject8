def jogar():
    print('################################')
    print('    Bem vindo o jogo da Forca   ')
    print('################################')

    palavra_secreta = 'morango'
    enforcou = False
    acertou = False


    while(not enforcou and not acertou):

        chute = input('Qual letra? ')

        index = 1
        for letra in palavra_secreta:
            if(chute == letra):
                print('Encontrei a letra {} na posição: {}'.format(letra, index))
            index = index + 1


        print(' jogando ...')


    print('Fim de Jogo ')


if(__name__ == '__main__'):
    jogar()