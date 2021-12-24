from random import randint

cores = {
    'reset':'\033[m',
    'vermelho':'\033[0;31m',
    'vermelho_erro':'\033[1;31m',
    'verde':'\033[1;32m',
    'sublinhado':'\033[4;37m',
    'azul':'\033[0;36m'
}

print('-~-'*10, f'-~-  {cores["azul"]}Jogo da Adivinhação!{cores["reset"]}  -~-', '-~-'*10, sep='\n', end='\n\n')

numero_secreto = randint(0, 100)
tentativas = 3

for rodada in range(1, tentativas + 1):
    
    print(f'Tentativa {rodada} de {tentativas}', end='\n\n')

    chute_jogador = int(input('Digite um número entre 1 e 100: '))
    
    if chute_jogador < 1 or chute_jogador > 100:
        
        print('\n', f'{cores["vermelho_erro"]}VOCÊ DEVE DIGITAR UM NÚMERO ENTRE 1 E 100!{cores["reset"]}', sep='', end='\n\n')
        continue

    acertou = chute_jogador == numero_secreto
    menor   = chute_jogador < numero_secreto
    maior   = chute_jogador > numero_secreto

    if acertou: 
        
        print(f'\n{cores["verde"]}Você acertou!{cores["reset"]}', end='\n\n')
        break

    else: 
        if maior: print(f'\n{cores["vermelho"]}Você errou!{cores["reset"]} Seu chute foi maior que o {cores["sublinhado"]}número secreto.{cores["reset"]}', end='\n\n')
        if menor: print(f'\n{cores["vermelho"]}Você errou!{cores["reset"]} Seu chute foi menor que o {cores["sublinhado"]}número secreto.{cores["reset"]}', end='\n\n')
        
    
print('-~-'*10, f'-~-~-~-  {cores["azul"]}Fim de jogo!{cores["reset"]}  -~-~-~-', '-~-'*10, sep='\n')