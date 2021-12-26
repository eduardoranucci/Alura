import forca
import adivinhacao


def escolhe_jogo():

    cores = {
        'reset': '\033[m',
        'vermelho': '\033[0;31m',
        'vermelho_erro': '\033[1;31m',
        'verde': '\033[0;32m',
        'verde_negrito': '\033[1;32m',
        'sublinhado': '\033[4;37m',
        'azul': '\033[0;36m',
        'amarelo': '\033[0;33m'
    }

    print('-~-'*11, f'-~-~-  {cores["azul"]} Escolha seu jogo! {cores["reset"]}  -~-~-', '-~-'*11, sep='\n', end='\n\n')
    
    print('(1) Forca (2) Adivinhação', end='\n\n')

    jogo = int(input('Qual jogo você quer jogar? '))

    if jogo == 1:
        print('\nIniciando forca...')
        forca.jogar()
        
    elif jogo == 2:
        print('\nIniciando adivinhação...', end='\n\n')
        adivinhacao.jogar()
        
    else:
        print(f'{cores["vermelho_erro"]}\nTente novamente{cores["reset"]}', end='\n\n')
    

if __name__ == '__main__':
    escolhe_jogo()
