from pprint import pprint


class Cliente:

    def __init__(self, nome, cpf, profissao):
        self.nome = nome
        self.cpf = cpf
        self.profissao = profissao


# cliente = Cliente('Dio Brando', '123.456.789-00', 'Dev')
# pprint(cliente.__dict__, width=40)


class ContaCorrente:

    total_contas_criadas = 0
    taxa_operacao = None

    def __init__(self, cliente, agencia, numero):
        self.__saldo = 100
        self.__agencia = 0
        self.__numero = 0

        self.cliente = cliente
        self.__set_agencia(agencia)
        self.__set_numero(numero)

        ContaCorrente.total_contas_criadas += 1
        ContaCorrente.taxa_operacao = 30 / ContaCorrente.total_contas_criadas

    @property
    def agencia(self):
        return self.__agencia

    def __set_agencia(self, valor):
        if not isinstance(valor, int):
            raise ValueError('Agencia deve ser um inteiro.', valor)
        if valor <= 0:
            raise ValueError('Agencia deve ser maior que zero.')

        self.__agencia = valor

    @property
    def numero(self):
        return self.__numero

    def __set_numero(self, valor):
        if not isinstance(valor, int):
            raise ValueError('Numero deve ser um inteiro.')
        if valor <= 0:
            raise ValueError('Numero deve ser maior que zero.')

        self.__numero = valor

    @property
    def saldo(self):
        return self.__saldo

    def __set_saldo(self, valor):
        if not isinstance(valor, int):
            raise ValueError('Saldo deve ser um inteiro.')
        if valor <= 0:
            raise ValueError('Saldo deve ser maior que zero.')

        self.__saldo = valor

    def transferir(self, valor, favorecido):
        favorecido.depositar(valor)

    def sacar(self, valor):
        self.saldo -= valor

    def depositar(self, valor):
        self.saldo += valor


def main():

    contas = []

    while True:
        try:
            nome = input('Nome do cliente: ')
            agencia = int(input('Número da agência: '))
            numero = int(input('Número da conta corrente: '))
            cliente = Cliente(nome, None, None)
            conta_corrente = ContaCorrente(cliente, agencia, numero)
            contas.append(conta_corrente)
            print()
        except ValueError as E:
            print(type(E.args[1]))
            exit()
        except KeyboardInterrupt:
            print(f'\n\n{len(contas)}(s) contas criadas')
            exit()


if __name__ == '__main__':
    main()
