from random import randint


def jogar():
    cores = {

        'reset': '\033[m',
        'vermelho': '\033[0;31m',
        'vermelho_erro': '\033[1;31m',
        'verde': '\033[0;32m',
        'verde_negrito': '\033[1;32m',
        'sublinhado': '\033[4;37m',
        'azul': '\033[0;36m',
        'amarelo': '\033[0;33m',
        'roxo': '\033[0;35m'

    }

    print('-~-' * 10, f'-~-  {cores["azul"]}Jogo da Adivinhação!{cores["reset"]}  -~-', '-~-' * 10, sep='\n',
          end='\n\n')

    print('Qual nível de dificuldade?',
          f'\n\n{cores["verde"]}(1) Fácil {cores["amarelo"]}(2) Médio {cores["vermelho"]}(3) Difícil {cores["roxo"]}'
          f'(4) Personalizado{cores["reset"]}',
          end='\n\n')

    numero_maximo = 100

    try:
        nivel = int(input('Defina o nível: '))
    except ValueError:
        nivel = 3
    print('\n', end='')

    if nivel == 1:
        tentativas = 20
    elif nivel == 2:
        tentativas = 10
    elif nivel == 3:
        tentativas = 5
    elif nivel == 4:

        print('Deixe em branco para selecionar o padrão.', end='\n\n')

        try:
            numero_maximo = int(input('Defina o número máximo aleatório (Padrão: 100): '))
        except ValueError:
            numero_maximo = 100
        try:
            tentativas = int(input('Defina o número de tentativas (Padrão: 5): '))
        except ValueError:
            tentativas = 5

    else:
        tentativas = 5

    numero_secreto = randint(0, numero_maximo)

    pontos = 1000

    for rodada in range(1, tentativas + 1):

        print(f'Tentativa {rodada} de {tentativas}', end='\n\n')

        chute_jogador = int(input(f'Digite um número entre 1 e {numero_maximo}: '))

        if chute_jogador < 1 or chute_jogador > numero_maximo:
            print('\n',
                  f'{cores["vermelho_erro"]}VOCÊ DEVE DIGITAR UM NÚMERO ENTRE 1 E {numero_maximo}!{cores["reset"]}',
                  sep='', end='\n\n')
            continue

        acertou = chute_jogador == numero_secreto
        menor = chute_jogador < numero_secreto
        maior = chute_jogador > numero_secreto

        if acertou:

            print(f'\n{cores["verde_negrito"]}Você acertou!{cores["reset"]} e fez {pontos} pontos!', end='\n\n')
            break

        else:
            if maior:
                print(
                    f'\n{cores["vermelho"]}Você errou!{cores["reset"]} Seu chute foi MAIOR que o '
                    f'{cores["sublinhado"]}número secreto.{cores["reset"]}',
                    end='\n\n')
            elif menor:
                print(
                    f'\n{cores["vermelho"]}Você errou!{cores["reset"]} Seu chute foi MENOR que o '
                    f'{cores["sublinhado"]}número secreto.{cores["reset"]}',
                    end='\n\n')

            pontos_perdidos = abs(numero_secreto - chute_jogador)
            pontos -= pontos_perdidos

    print('-~-' * 10, f'-~-~-~-  {cores["azul"]}Fim de jogo!{cores["reset"]}  -~-~-~-', '-~-' * 10, sep='\n')


if __name__ == '__main__':
    jogar()
