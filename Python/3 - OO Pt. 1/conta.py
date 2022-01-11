class Conta:

    def __init__(self, numero, titular, saldo, limite=1000.0):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print(f'Saldo: R${self.__saldo}, do titular {self.__titular}.')

    def deposita(self, valor):
        self.__saldo += valor

    def __saldo_suficiente(self, valor):
        valor_disponivel = self.__saldo + self.limite
        return valor <= valor_disponivel

    def saca(self, valor):
        if self.__saldo_suficiente(valor):
            self.__saldo -= valor
        else:
            print('Saldo insuficiente')

    def transfere(self, destino, valor):
        self.saca(valor)
        destino.deposita(valor)

    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @staticmethod
    def codigo_banco():
        return '001'

    @staticmethod
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}

    @limite.setter
    def limite(self, limite):
        self.__limite = limite
