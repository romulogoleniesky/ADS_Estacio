# TIPOS DE RANGE:
# Range simples: "range(3)", terá uma sequência de : 0, 1, 2. (3 passos começando em 0)
print('Range simples:')
for a in range(3):
    print(a)

print('Range com início e fim:')
# Range com início e fim : "range(2,5)" : 2, 3, 4. (começa no passo 2)
for b in range(2, 5):
    print(b)
print('Range com início, fim e passo:')
# Range com início,fim e passo: range(1,6,2): 1, 3, 5(começa no passo 1 e anda dois passos)
for c in range(1,6,2):
    print(c)
