try:
    with open('contatos.csv') as arquivo_contato:

        for linha in arquivo_contato:
            print(linha, end='')

except FileNotFoundError:
    print('Arquivo não encontrado.')

except PermissionError:
    print('Sem permissão de escrita.')

