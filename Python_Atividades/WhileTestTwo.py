#   TEST WITH WHILE - PART TWO
n1 = int(input('Digite um número : '))
n2 = int(input('Digite outro número : '))
s = n1 + n2
res = int(input('Qual é o resultado da Soma desses números? :'))
while res != s:
    res = int(input('Você errou! Tente novamente'))
print('Você acertou, Parabéns!')
