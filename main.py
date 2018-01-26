from cliente import Cliente
from conta import Conta

cliente1 = Cliente('0x00s4d', '011.001.111-01', 22)
print(cliente1)

conta1 = Conta(cliente1, 2000.55, 3000)
print(conta1.cliente.nome, conta1.consulta_saldo())
conta1.depositar(550)
print(conta1.consulta_saldo())
conta1.sacar(4000)
print(conta1.consulta_saldo())
conta1.sacar(2000)
print(conta1.consulta_saldo())

