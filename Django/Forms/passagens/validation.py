def origem_destino_iguais(origem, destino, lista_erros):
    """ Verifica se origem e destino são iguais """

    if origem == destino:
        lista_erros['destino'] = 'Origem e destino não podem ser iguais.'

def campo_tem_numero(valor_campo, campo, lista_erros):
    """ Verifica se um campo tem algum dígito numérico """

    if any(char.isdigit() for char in valor_campo):
        lista_erros[campo] = f'{campo.capitalize()} não pode conter números.'

def volta_menor_que_ida(ida, volta, lista_erros):
    ''' Verifica se a data de ida é maior que a data de volta '''
    
    if ida > volta:
        lista_erros['data_volta'] = 'Data de volta não pode ser menor que a data de ida.'

def ida_menor_que_hoje(ida, hoje, lista_erros):
    ''' Verifica se a data de ida é menor que a data de hoje '''

    if ida < hoje:
        lista_erros['data_ida'] = 'Data de ida não pode ser menor que data de hoje.'

