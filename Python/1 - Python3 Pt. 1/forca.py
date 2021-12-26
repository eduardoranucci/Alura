

def jogar():
    
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

    print('-~-'*10, f'-~-~-~  {cores["azul"]}Jogo da Forca!{cores["reset"]}  ~-~-~-', '-~-'*10, sep='\n', end='\n\n')
    
    print('-~-'*10, f'-~-~-~-  {cores["azul"]}Fim de jogo!{cores["reset"]}  -~-~-~-', '-~-'*10, sep='\n')
    

if __name__ == '__main__': jogar()