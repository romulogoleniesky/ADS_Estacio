# Classes em Python: Operações das contas.

class Conta:
    def __init__(self, clientes, numero, saldo):
        self.clientes = clientes
        self.numero = numero
        self.saldo = saldo
    def depositar(self, valor):
        self.saldo += valor
    def sacar(self, valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            return True
    def transfereValor(self, contaDestino, valor):
        if self.saldo < valor:
            return ("Não existe saldo suficiente!")
        else:
            contaDestino.depositar(valor)
            self.saldo -= valor
            return("Transferência Realizada!")
    def gerarSaldo(self):
        print(f'Número: {self.numero}\n Saldo: R${self.saldo}')




