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

    def saca(self, valor):
        self.__saldo -= valor

    def tranfere(self, destino, valor):
        self.saca(valor)
        destino.deposita(valor)
