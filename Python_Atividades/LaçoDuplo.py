while True:
    print('Você está no primeiro laço.')
    opcao1 = input('Deseja sair dele? Digite SIM para isso. ')
    if opcao1 == 'SIM':
        break
    else:
        while True:
            print('Voçê está no segundo laço.')
            opcao2 = input('Deseja sair dele? Digite SIM.')
            if opcao2 =='SIM':
                break
        print('você saiu do segundo laço.')
print('Voçê saiu do primeiro laço.')
