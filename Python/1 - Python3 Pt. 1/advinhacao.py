print('-~-'*10)
print('     Jogo da Adivinhação')
print('-~-'*10, end='\n\n')

numero_secreto = 47

chute_jogador = int(input('Digite um número: '))

if numero_secreto == chute_jogador: print('Você acertou!')
else: print(f'Você errou, o número certo é {numero_secreto}')