from conta import Conta

conta = Conta(117, 'Eduardo Ranucci', 100.0)
conta2 = Conta(123, 'Nico', 200.0)

conta.deposita(15.0)
conta.extrato()

print()

conta2.tranfere(conta, 10.0)
conta.extrato()
conta2.extrato()
