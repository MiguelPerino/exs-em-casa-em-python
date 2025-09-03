from time import sleep
lista_todos_produtos = []

def menu_produtos():
    
    while True:
        print('\n\033[30;47m---Área de Produtos---\033[0m ')
        print('1 - Cadastrar Produto')
        print('2 - Consultar Produto')
        print('3 - Listar todos Produtos')
        print('0 - Sair')

        option = input('Informe a opção desejada: ')
        
        if option == '1':
            while True:
                try:
                    product_name = input('\nInforme o nome do produto: ')
                    product_price = float(input(f'Informe o preço do produto "{product_name}": R$'))
                    sleep(0.3)
                    print('\n\033[0;32mProduto cadastrado com sucesso\033[0m!')

                    product_dic = {
                        'nome': product_name,
                        'preço': product_price
                    }

                    lista_todos_produtos.append(product_dic)
                except ValueError:
                    print('Entrada incompatível, tente novamente...')
                    continue

                wish_continue = input('\nDeseja continuar (s/n)? ').lower()
                if wish_continue == 's' or wish_continue == 'sim':
                    continue
                elif wish_continue == 'n' or wish_continue == 'nao':
                    print('Voltando pra Área de Produtos!')
                    break
                else:
                    print('Entrada incompátivel, tente novamente...')

        elif option == '2':
            if not lista_todos_produtos:
                print('\nNenhum produto cadastrado ainda!')
                continue

            while True:
                product_consulting = input('\nInforme o nome do produto que deseja consultar: ').lower()

                founded = False
                for product in lista_todos_produtos:
                    if product['nome'] == product_consulting:
                        print(f"O produto: {product_consulting} custa R${product['preço']:.2f} ")
                        founded = True
                        break
                if not founded:
                    print(f'O produto "{product_consulting}" não foi encontrado.')


                wish_continue_2 = input('\nDeseja consultar outro (s/n)? ').lower()
                if wish_continue_2 == 's' or wish_continue_2 == 'sim':
                    continue
                elif wish_continue_2 == 'n' or wish_continue_2 == 'nao': 
                    print('Voltando pra Área de Produtos!')
                    sleep(0.4)
                    break
                else:
                    print('Entrada incompátivel, tente novamente...')
                    break

        elif option == '3':
            if not lista_todos_produtos:
                print('\nA lista de produtos está vazia, nenhum foi cadastrado ainda!')

            else:
                print('\n--- Tabela com todos os produtos ---')
                for i, produtos in enumerate(lista_todos_produtos):
                    print(f'{i + 1}° produto: {produtos["nome"]}')

            input('\nPressione Enter para voltar na Área de Produtos!')


        elif option == '0':
            print('\nVoltando pro menu principal...!')
            print()
            sleep(0.4)
            break

        else: 
            print('Entrada incompátivel, tente novamente...')
all_sales = [] 
def menu_vendas():
       
    while True:
        print('\n\033[30;47m---Área de Vendas---\033[0m ')
        print('1 - Cadastrar Venda')
        print('2 - Consultar Venda')
        print('3 - Listar todas as Vendas')
        print('0 - Sair')

        option = input('Informe a opção desejada: ')
        
        if option == '1':

            client_name = input('Informe o nome do cliente (ou digite "sair"): ').title().strip()
            date = input('Data em que foi vendido o produto (dd/mm/aaaa): ').strip()
            contador = 1
            #Lista de produtos comprados
            product_list = []
            while True:
                products_sold = input(f'Informe o nome do {contador}° produto que {client_name} comprou (ou digite "sair" caso não tenha produto cadastrado): ').strip().lower()
                if products_sold == 'sair':
                    break
                
                found = False
                for product in lista_todos_produtos:
                    if products_sold == product['nome'].lower():
                        quantity = int(input(f'Quantidade do produto "{products_sold}" vendido: '))
                        product_list.append({
                            'name': product['nome'],
                            'quantity': quantity,
                            'price': product['preço']
                        })
                        found = True
                        contador += 1
                        break

                if not found:
                    print('Produto não cadastrado!')
                    
            if product_list:
                inf_sales = {
                    'client': client_name,
                    'date': date,
                    'products': product_list    #chamar product['name'] product['quantity'] 
                }
                all_sales.append(inf_sales)
                print('\nVenda cadastrada com sucesso!')
            else: 
                print('\nNenhum produto adicionado. Venda nao cadastrada')

        elif option == '2':    
            if not all_sales:
                print('\nNenhuma venda cadastrada!')
                continue
            

            ## ADICIONAR SET(CONJUNTO) PARA NAO REPETIR OS NOMES
            print('CLIENTES: ')
            for client in all_sales:
                print(client['client'], end = ' | ')
            print()

            search_client = input('Informe o nome do cliente que deseja consultar: ')

            
            found = False
            total = 0
            for information in all_sales:
                if search_client == information['client']:
                    if not found:
                        print(f"\nCliente: {search_client}")
                        found = True

                    print(f"Data: {information['date']}")
                    for product in information['products']:
                        print(f"Produto: {product['name']} - Quantidade: {product['quantity']}")
                        total += product['price'] * product['quantity']
            if found:
                print(f'\nTotal gasto pelo cliente: {total:.2f}')       
            else:
                print('\nCliente não encontrado!')        
            
            if not found:
                print('\nCliente não encontrado')
        ##    
        elif option == '3':
            print('\nLista de todos os clientes e seus produtos comprados: ')
            print()
            for dictionary in all_sales:
                print(f"Nome: {dictionary['client']} - Data: {dictionary['date']}")
                for products in dictionary['products']:
                    print(f"Produto: {products['name']} - Quantidade: {products['quantity']} - Preço: {products['price']}")

            #QUEM É O CLIENTE QUE MAIS GASTOU
            ...
        elif option == '0':
            print('Voltando pro Menu Principal...!')
            sleep(0.4)
            break

        else:
            print('Entrada incompatível!')
            

def menu_principal():
    while True:
        print('\033[30;47m===Sistema de controle de vendas!===\033[0m')
        print('\nMenu principal: ')
        print('1 - Área de produtos')
        print('2 - Área de vendas')
        print('0 - Sair')

        option = input('Informe onde quer entrar: ')

        match option:
            case '1':
                menu_produtos()
                
            case '2':
                menu_vendas()
            case '0':
                print('\nSaindo do programa, até logo...')
                break
            case _:
                print('\nEntrada incompatível, tente novamente...')
                print()


menu_principal()

