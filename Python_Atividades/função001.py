valor = 0
saldo = 100.00
def sacar(valor):
    return saldo - valor
def poupar(juros):
    return saldo * juros
s = 0
op = input(f'Seu Saldo é R${saldo} \nSacar(S)\nPoupar(P)')

if op == 'S':
    s = sacar(100)
elif op == 'P':
    s = poupar(1.10)
else:
    while op != 'S' or 'P':
        print('Digite "S" para Sacar ou "P" para Poupar')
        break
print(f'{s:.2f}')