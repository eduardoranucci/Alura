from random import randint

cores = {
    'reset':'\033[m',
    'vermelho':'\033[0;31m',
    'vermelho_erro':'\033[1;31m',
    'verde':'\033[0;32m',
    'verde_negrito':'\033[1;32m',
    'sublinhado':'\033[4;37m',
    'azul':'\033[0;36m',
    'amarelo': '\033[0;33m'
}

print('-~-'*10, f'-~-  {cores["azul"]}Jogo da Adivinhação!{cores["reset"]}  -~-', '-~-'*10, sep='\n', end='\n\n')

print('Qual nível de dificuldade?', f'\n\n{cores["verde"]}(1) Fácil {cores["amarelo"]}(2) Médio {cores["vermelho"]}(3) Difícil{cores["reset"]}', end='\n\n')

nivel = int(input('Defina o nível: '))
print('\n', end='')

if nivel == 1: tentativas = 20
elif nivel == 2: tentativas = 10
else: tentativas = 5

numero_secreto = randint(0, 100)

pontos = 1000

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
        
        print(f'\n{cores["verde_negrito"]}Você acertou!{cores["reset"]} e fez {pontos}!', end='\n\n')
        break

    else: 
        if maior: print(f'\n{cores["vermelho"]}Você errou!{cores["reset"]} Seu chute foi MAIOR que o {cores["sublinhado"]}número secreto.{cores["reset"]}', end='\n\n')
        elif menor: print(f'\n{cores["vermelho"]}Você errou!{cores["reset"]} Seu chute foi MENOR que o {cores["sublinhado"]}número secreto.{cores["reset"]}', end='\n\n')
        
        pontos_perdidos = abs(numero_secreto - chute_jogador)
        pontos -= pontos_perdidos
        
    
print('-~-'*10, f'-~-~-~-  {cores["azul"]}Fim de jogo!{cores["reset"]}  -~-~-~-', '-~-'*10, sep='\n')