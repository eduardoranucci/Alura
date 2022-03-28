arquivo_contato = open('contatos.csv')

for linha in arquivo_contato:
    print(linha, end='')
