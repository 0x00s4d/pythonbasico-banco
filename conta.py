class Conta:

    def __init__(self, cliente, saldo, limite):
        self.cliente = cliente
        self.saldo = saldo
        self.limite = 0-limite

    def depositar(self, quantidade):
        if quantidade > self.limite:
            self.saldo += quantidade
            print('Depositou ', quantidade)
        else:
            print('Nao foi possivel depositar.')

    def consulta_saldo(self):
        return self.saldo

    def sacar(self, quantidade):
        if (self.saldo - quantidade) < self.limite:
            print('Saldo insuficiente.')
        else:
            self.saldo -= quantidade
            print('Saque ', quantidade)

