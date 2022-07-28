<<<<<<< HEAD
class OperacaoFinanceiraError(Exception):
    pass


class SaldoInsuficienteError(OperacaoFinanceiraError):
    
    def __init__(self, message='', saldo=None, valor=None, *args, **kwargs):
        self.valor = valor
        self.saldo = saldo

        msg = 'Saldo insulficiente para efetuar a transação\n' \
              f'Saldo atual: {self.saldo}, Valor a ser sacado: {self.valor}'

        self.msg = message or msg

        super(SaldoInsuficienteError, self).__init__(self.msg, self.valor, self.saldo, *args)
=======
class OperacaoFinanceiraError(Exception):
    pass


class SaldoInsuficienteError(OperacaoFinanceiraError):
    
    def __init__(self, message='', saldo=None, valor=None, *args, **kwargs):
        self.valor = valor
        self.saldo = saldo

        msg = 'Saldo insulficiente para efetuar a transação\n' \
              f'Saldo atual: {self.saldo}, Valor a ser sacado: {self.valor}'

        self.msg = message or msg

        super(SaldoInsuficienteError, self).__init__(self.msg, self.valor, self.saldo, *args)
>>>>>>> 32b7d5a6b7bc21f564eec73ca071ae4cf8208acd
