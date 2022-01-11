from conta import Conta
from cliente import Cliente

conta = Conta(117, 'Eduardo Ranucci', 100.0)
conta2 = Conta(123, 'Nico', 200.0)

cliente = Cliente('dio')

conta.deposita(15.0)
conta.extrato()

print()

conta2.transfere(conta, 10.0)
conta.extrato()
conta2.extrato()

conta.saldo

cliente.nome = 'jojo'
cliente.nome

conta.saca(2000)
conta.extrato()

conta.codigo_banco
