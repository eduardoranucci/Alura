
def jogar():

    cores = {
        'reset': '\033[m',
        'vermelho': '\033[0;31m',
        'verde_negrito': '\033[1;32m',
        'sublinhado': '\033[4m',
        'azul': '\033[0;36m'
    }

    print('-~- ' * 10, f'-~-~-~-~-~  {cores["azul"]}-Jogo da Forca-{cores["reset"]}  ~-~-~-~-~-', '-~- ' * 10, sep='\n',
          end='\n\n')

    palavra_secreta = 'banana'.upper()
    letras_acertadas = ['_' for letra in palavra_secreta]
    enforcou = False
    acertou = False
    tentativas = 6

    print(letras_acertadas, end='\n\n')

    while not enforcou and not acertou:

        chute = input('Qual letra? ').strip().upper()

        if chute in palavra_secreta:
            i = 0
            for letra in palavra_secreta:
                if chute == letra:
                    letras_acertadas[i] = letra
                i += 1
        else:
            tentativas -= 1
            if tentativas == 0:
                pass
            else:
                print(f'\n{cores["vermelho"]}Você errou, faltam {tentativas} tentativas.{cores["reset"]}')

        enforcou = tentativas == 0
        acertou = '_' not in letras_acertadas

        print('\n', end='')
        print(letras_acertadas, end='\n\n')

    if acertou:
        print(f'{cores["verde_negrito"]}Você ganhou!{cores["reset"]}', end='\n\n')
    else:
        print(f'{cores["vermelho"]}Você perdeu!{cores["reset"]}', end='\n\n')

    print('-~-' * 10, f'-~-~-~-  {cores["azul"]}Fim de jogo!{cores["reset"]}  -~-~-~-', '-~-' * 10, sep='\n')


if __name__ == '__main__':
    jogar()
