# Arquivo da Classe Conta.

class Conta:
    def __init__(self, numero, cpf, nomeTitular, saldo):
        self.numero = numero
        self.cpf = cpf
        self.nomeTitular = nomeTitular
        self.saldo = saldo
    def __depositar__(self, valor):
        self.saldo += valor
    def __sacar__(self, valor):
        self.saldo -= valor
    def __gerarextrato__(self):
        print(f'número:{self.numero}\n CPF: {self.cpf}\n Saldo: {self.saldo}')
c1 = Conta(1, 1, "João", 1000)
print(c1.saldo)
print(c1.nomeTitular)
print(c1.saldo)
Conta.__depositar__(c1, 300)
print(c1.saldo)
Conta.__sacar__(c1, 900)
print(c1.saldo)
Conta.__gerarextrato__(c1)
c1.__gerarextrato__()
