from random import randint

cores = {
        'reset': '\033[m',
        'vermelho': '\033[0;31m',
        'verde_negrito': '\033[1;32m',
        'sublinhado': '\033[4m',
        'azul': '\033[0;36m'
    }


def jogar():
    mostrar_msg_abertura()

    palavra_secreta = carrega_palavra_secreta()

    letras_acertadas = ['_' for letra in palavra_secreta]
    print(letras_acertadas, end='\n\n')

    enforcou = False
    acertou = False
    tentativas = 6

    while not enforcou and not acertou:

        chute = input('Qual letra? ').strip().upper()

        if chute in palavra_secreta:
            verifica_chute(chute, letras_acertadas, palavra_secreta)
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
        mostrar_msg_vitoria()
    else:
        mostrar_msg_derrota(palavra_secreta)


def mostrar_msg_abertura():
    print('-~- ' * 10, f'-~-~-~-~-~  {cores["azul"]}-Jogo da Forca-{cores["reset"]}  ~-~-~-~-~-', '-~- ' * 10, sep='\n',
          end='\n\n')


def mostrar_msg_encerramento():
    print('-~-' * 10, f'-~-~-~-  {cores["azul"]}Fim de jogo!{cores["reset"]}  -~-~-~-', '-~-' * 10, sep='\n')


def carrega_palavra_secreta():
    arquivo = open('palavras.txt', 'r', encoding='UTF-8')
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = randint(0, len(palavras))
    palavra_secreta = palavras[numero].upper()

    return palavra_secreta


def verifica_chute(chute, letras_acertadas, palavra_secreta):
    i = 0
    for letra in palavra_secreta:
        if chute == letra:
            letras_acertadas[i] = letra
        i += 1


def mostrar_msg_vitoria():
    print(f'{cores["verde_negrito"]}Você ganhou!{cores["reset"]}')


def mostrar_msg_derrota(palavra):
    print(f'{cores["vermelho"]}Você perdeu!{cores["reset"]}', end='\n\n')
    print(f'A palavra era {palavra}!')


if __name__ == '__main__':
    jogar()
