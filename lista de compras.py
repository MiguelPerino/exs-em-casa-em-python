from time import sleep

lista = []
print('Bem vindo a lista de compras!')
while True:
    try:
        escolha = input('\nInforme o que deseja fazer: \n [i]nserir [a]pagar [l]ista ou [s]air: ').lower()
        if escolha not in ['i', 'a', 'l', 's']:
            raise ValueError
        
        if escolha == 'i':
            print()
            valor = input('Digite oque quer adicionar na lista: ')
            lista.append(valor)
            sleep(0.3)
            print('\nItem adicionado com sucesso!')


        elif escolha == 'a':
            print('\nSua lista de compras: ')
            for i, valor in enumerate(lista):
                print(i, valor)
            try:
                apagar = int(input('\nQual índice deseja apagar: '))
                del lista[apagar]
                sleep(0.5)
                print('\nFeito, item apagado com sucesso!')

            except (ValueError, IndexError):
                print('\nÍndice indisponível na sua lista de compras!') 


        elif escolha == 'l':
            if not lista:
                print('Sua lista está vazia!')
            else:
                print('\nSua lista de compra: ')
                for i, valor in enumerate(lista):
                    print(i, valor)
        elif escolha == 's':
            print()
            print('Saindo... até logo!')
            break

    except ValueError:
        print()
        print('Valor de entrada incorreto, escolha uma entre as opções disponíveis...')
